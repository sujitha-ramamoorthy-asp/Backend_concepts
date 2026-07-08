from sqlalchemy.orm import Session

from app.models import Inventory
from app.models import InventoryStatus

from app.schemas import InventoryRequest


class InventoryService:

    @staticmethod
    def reserve(db: Session, request: InventoryRequest):

        # Simulate inventory failure
        if request.product_name.lower() == "laptop":
            raise Exception("Inventory unavailable")

        inventory = Inventory(
            order_id=request.order_id,
            product_name=request.product_name,
            quantity=request.quantity,
            status=InventoryStatus.RESERVED,
        )

        db.add(inventory)

        db.commit()

        db.refresh(inventory)

        return inventory

    @staticmethod
    def get_all(db: Session):

        return db.query(Inventory).all()
