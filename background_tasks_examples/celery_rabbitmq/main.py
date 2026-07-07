from fastapi import FastAPI, Depends
from models import Order
from sqlalchemy.orm import Session
from tasks import send_order_email
from schemas import OrderCreate
from database import Base, engine, get_db

app = FastAPI()

# Database configuration
DATABASE_URL="mysql+pymysql://admin:mypassword@localhost/test"



# Create tables
Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Application Started"}

@app.post("/orders")

def create_order(order: OrderCreate, db: Session = Depends(get_db)):

  

    order_obj = Order(
        customer_name=order.customer_name,
        product_name=order.product_name,
        customer_email=order.customer_email,
        quantity = order.quantity
    )

    db.add(order_obj)

    db.commit()

    db.refresh(order_obj)

    send_order_email.delay(
        order_obj.customer_email,
        order_obj.id
    )

    return {
        "message":"Order Created",
        "order_id":order_obj.id
    }