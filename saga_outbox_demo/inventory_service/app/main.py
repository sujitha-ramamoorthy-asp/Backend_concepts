from fastapi import FastAPI

from inventory_service.app.database import Base
from inventory_service.app.database import engine
# Import the model
from inventory_service.app.models import Inventory

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"service": "Inventory Service"}