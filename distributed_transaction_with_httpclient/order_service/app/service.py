from sqlalchemy.orm import Session

from app.models import Order
from app.models import OrderStatus
from app.schemas import OrderCreate
from app.config import settings
import httpx
from app.http_client import client

class OrderService:

    # @staticmethod
    # def create_order(
    #     db: Session,
    #     request: OrderCreate
    # ) -> Order:

    #     order = Order(
    #         customer_name=request.customer_name,
    #         product_name=request.product_name,
    #         quantity=request.quantity,
    #         amount=request.amount,
    #         status=OrderStatus.PENDING
    #     )

    #     db.add(order)

    #     db.commit()

    #     db.refresh(order)

    #     return order

    @staticmethod
    async def create_order(
        db: Session,
        request: OrderCreate
    ):

        # Step 1: Create Order
        order = Order(
            customer_name=request.customer_name,
            product_name=request.product_name,
            quantity=request.quantity,
            amount=request.amount,
            status=OrderStatus.PENDING
        )

        db.add(order)
        db.commit()
        db.refresh(order)

        print(f"Order {order.id} created")

        try:

            # Step 2: Call Payment Service
            payment_response = await client.post(
                f"{settings.PAYMENT_SERVICE}/payment",
                json={
                    "order_id": order.id,
                    "amount": order.amount
                }
            )

            payment_response.raise_for_status()

            print("Payment Success")

            # Step 3: Call Inventory Service
            inventory_response = await client.post(
                f"{settings.INVENTORY_SERVICE}/reserve",
                json={
                    "order_id": order.id,
                    "product_name": order.product_name,
                    "quantity": order.quantity
                }
            )

            inventory_response.raise_for_status()

            print("Inventory Reserved")

            order.status = OrderStatus.COMPLETED

            db.commit()

            db.refresh(order)

            print("Saga Completed")

            return order

        except httpx.HTTPStatusError as ex:

            print("Business Error:", ex.response.text)

            # Compensation
            await client.post(
                f"{settings.PAYMENT_SERVICE}/refund/{order.id}"
            )

            order.status = OrderStatus.CANCELLED

            db.commit()

            db.refresh(order)

            return order

        except httpx.RequestError as ex:

            print("Network Error:", ex)

            order.status = OrderStatus.CANCELLED

            db.commit()

            db.refresh(order)

            return order

    @staticmethod
    def get_order(db: Session, order_id: int):

        return db.query(Order).filter(Order.id == order_id).first()

    @staticmethod
    def get_all_orders(db: Session):

        return db.query(Order).order_by(Order.id).all()

    @staticmethod
    def update_status(db: Session, order_id: int, status: OrderStatus):

        order = db.query(Order).filter(Order.id == order_id).first()

        if not order:
            return None

        order.status = status

        db.commit()

        db.refresh(order)

        return order

    @staticmethod
    def cancel_order(db: Session, order_id: int):

        return OrderService.update_status(db, order_id, OrderStatus.CANCELLED)
