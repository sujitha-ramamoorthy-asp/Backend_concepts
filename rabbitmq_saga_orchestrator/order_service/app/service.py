from sqlalchemy.orm import Session

from app.models import Order
from app.schemas import OrderRequest

from common.publisher import publish_event
from common.events import (
    ORDER_CREATED,
    INVENTORY_RESERVE
)


class OrderService:

    @staticmethod
    async def create_order(
        db: Session,
        request: OrderRequest
    ):
        """
        Create a new order and start the Saga.
        """

        order = Order(
            customer=request.customer,
            amount=request.amount,
            status="PENDING"
        )

        db.add(order)
        db.commit()
        db.refresh(order)

        print(f"Order Created : {order.id}")

        # Start Saga
        await publish_event(
            routing_key=ORDER_CREATED,
            payload={
                "order_id": order.id,
                "customer": order.customer,
                "amount": order.amount
            }
        )

        print("Published -> order.created")

        return order

    @staticmethod
    async def handle_payment_completed(
        db: Session,
        event: dict
    ):
        """
        Payment succeeded.
        Orchestrator decides the next step.
        """

        order = (
            db.query(Order)
            .filter(Order.id == event["order_id"])
            .first()
        )

        if not order:
            print("Order not found")
            return

        print(
            f"Payment completed for Order {order.id}"
        )

        await publish_event(
            routing_key=INVENTORY_RESERVE,
            payload={
                "order_id": order.id
            }
        )

        print("Published -> inventory.reserve")

    @staticmethod
    def handle_inventory_completed(
        db: Session,
        event: dict
    ):
        """
        Inventory reserved successfully.
        Complete the Order.
        """

        order = (
            db.query(Order)
            .filter(Order.id == event["order_id"])
            .first()
        )

        if not order:
            print("Order not found")
            return

        order.status = "COMPLETED"

        db.commit()

        print(
            f"Order {order.id} COMPLETED"
        )

    @staticmethod
    async def handle_inventory_failed(
        db: Session,
        event: dict
    ):
        """
        Inventory reservation failed.

        Start compensation.
        """

        order = (
            db.query(Order)
            .filter(Order.id == event["order_id"])
            .first()
        )

        if not order:
            print("Order not found")
            return

        print(
            f"Inventory failed for Order {order.id}"
        )

        await publish_event(
            routing_key="refund.request",
            payload={
                "order_id": order.id
            }
        )

        print("Published -> refund.request")

    @staticmethod
    def handle_refund_completed(
        db: Session,
        event: dict
    ):
        """
        Refund completed.

        Cancel the Order.
        """

        order = (
            db.query(Order)
            .filter(Order.id == event["order_id"])
            .first()
        )

        if not order:
            print("Order not found")
            return

        order.status = "CANCELLED"

        db.commit()

        print(
            f"Order {order.id} CANCELLED"
        )