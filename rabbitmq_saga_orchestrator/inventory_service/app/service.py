from sqlalchemy.orm import Session

from app.models import Inventory

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
        """
        Reserve inventory.

        For demo:
        Odd Order Id  -> Success
        Even Order Id -> Failure
        """

        order_id = event["order_id"]

        # Demo failure
        if order_id % 2 == 0:

            print(f"Inventory NOT available for Order {order_id}")

            await publish_event(
                routing_key=INVENTORY_FAILED,
                payload={
                    "order_id": order_id
                }
            )

            print("Published -> inventory.failed")

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

        print(f"Inventory Reserved for Order {order_id}")

        await publish_event(
            routing_key=INVENTORY_COMPLETED,
            payload={
                "order_id": order_id
            }
        )

        print("Published -> inventory.completed")