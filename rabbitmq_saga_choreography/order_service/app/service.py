from sqlalchemy.orm import Session

from .models import Order
from .schemas import OrderRequest

from common.publisher import publish_event
from common.events import ORDER_CREATED
from common.correlation import create_saga_id


class OrderService:

    @staticmethod
    async def create_order(
        db: Session,
        request: OrderRequest
    ):

        order = Order(
            customer=request.customer,
            amount=request.amount,
            status="PENDING"
        )

        db.add(order)
        db.commit()
        db.refresh(order)

        saga_id = create_saga_id()

        print("\n================================")
        print("NEW ORDER CREATED")
        print("================================")
        print(f"Order ID : {order.id}")
        print(f"Saga ID  : {saga_id}")

        await publish_event(

            routing_key=ORDER_CREATED,

            payload={

                "saga_id": saga_id,

                "order_id": order.id,

                "customer": order.customer,

                "amount": order.amount

            }

        )

        return order

    @staticmethod
    def inventory_completed(
        db: Session,
        event: dict
    ):

        order = (
            db.query(Order)
            .filter(Order.id == event["order_id"])
            .first()
        )

        if order is None:

            print(
                f"Order {event['order_id']} not found."
            )

            return

        # Idempotency
        if order.status == "COMPLETED":

            print(
                f"Order {order.id} already completed."
            )

            return

        order.status = "COMPLETED"

        db.commit()

        print("\n================================")
        print("ORDER COMPLETED")
        print("================================")
        print(f"Saga ID  : {event['saga_id']}")
        print(f"Order ID : {order.id}")
        print(f"Status   : {order.status}")

    @staticmethod
    def payment_refunded(
        db: Session,
        event: dict
    ):

        order = (
            db.query(Order)
            .filter(Order.id == event["order_id"])
            .first()
        )

        if order is None:

            print(
                f"Order {event['order_id']} not found."
            )

            return

        # Idempotency
        if order.status == "CANCELLED":

            print(
                f"Order {order.id} already cancelled."
            )

            return

        order.status = "CANCELLED"

        db.commit()

        print("\n================================")
        print("ORDER CANCELLED")
        print("================================")
        print(f"Saga ID  : {event['saga_id']}")
        print(f"Order ID : {order.id}")
        print(f"Status   : {order.status}")