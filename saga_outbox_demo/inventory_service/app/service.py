from inventory_service.app.models import Inventory


class InventoryService:

    @staticmethod
    def reserve_inventory(db, product, quantity):

        print("reserve")

        item = db.query(Inventory).filter(
            Inventory.product == product
        ).first()

        if item is None:
            return False

        if item.available_quantity < quantity:
            return False

        item.available_quantity -= quantity

        db.commit()

        return True