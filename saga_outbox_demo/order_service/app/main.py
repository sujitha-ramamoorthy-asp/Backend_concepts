from fastapi import FastAPI
from fastapi import Depends

from sqlalchemy.orm import Session

from order_service.app.database import Base
from order_service.app.database import engine
from order_service.app.database import get_db

from order_service.app.schemas import OrderRequest
from order_service.app.service import OrderService

#from order_service.app.models import Order, Outbox

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/orders")
def create_order(
        request: OrderRequest,
        db: Session = Depends(get_db)
):

    order = OrderService.create_order(
        db,
        request
    )

    return {
        "order_id": order.id,
        "status": order.status
    }