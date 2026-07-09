import json

from app.models import Order
from app.models import Outbox

from common.events import ORDER_CREATED


class OrderService:

    @staticmethod
    def create_order(db, request):

        order = Order(
            product=request.product,
            quantity=request.quantity,
            status="CREATED"
        )

        db.add(order)

        db.flush()

        payload = json.dumps({
            "order_id": order.id,
            "product": order.product,
            "quantity": order.quantity
        })

        outbox = Outbox(
            event_type=ORDER_CREATED,
            payload=payload,
            published=False
        )

        db.add(outbox)

        db.commit()

        db.refresh(order)

        return order