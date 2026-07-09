from sqlalchemy.orm import Session

from .models import Inventory

from common.publisher import publish_event
from common.events import (
    INVENTORY_COMPLETED,
    INVENTORY_FAILED
)


class InventoryService:

    @staticmethod
    async def reserve_inventory(
        db: Session,
        event: dict
    ):

        order_id = event["order_id"]

        # Simulate failure
        if order_id % 2 == 0:

            print(
                f"Inventory NOT Available : {order_id}"
            )

            await publish_event(

                routing_key=INVENTORY_FAILED,

                payload={
                    "saga_id": event["saga_id"],
                    "order_id": order_id
                }

            )

            return

        existing_inventory = (

            db.query(Inventory)

            .filter(
                Inventory.order_id == order_id
            )

            .first()

        )

        if existing_inventory:

            print(

                f"Inventory already reserved for Order {order_id}"

            )

            return

        inventory = Inventory(

            order_id=order_id,

            product="Laptop",

            quantity=1,

            status="RESERVED"

        )

        db.add(inventory)

        db.commit()

        db.refresh(inventory)

        print(
            f"Inventory Reserved : {order_id}"
        )

        await publish_event(

            routing_key=INVENTORY_COMPLETED,

            payload={
                "saga_id": event["saga_id"],
                "order_id": order_id
            }

        )