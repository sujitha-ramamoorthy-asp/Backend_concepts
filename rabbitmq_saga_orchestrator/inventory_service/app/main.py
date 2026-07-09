from contextlib import asynccontextmanager

import asyncio

from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.consumer import start_consumer


@asynccontextmanager
async def lifespan(app: FastAPI):

    Base.metadata.create_all(bind=engine)

    consumer_task = asyncio.create_task(
        start_consumer()
    )

    print("Inventory Service Started")

    yield

    consumer_task.cancel()

    try:
        await consumer_task
    except asyncio.CancelledError:
        pass


app = FastAPI(
    title="Inventory Service",
    lifespan=lifespan
)


@app.get("/")
async def home():

    return {
        "message": "Inventory Service Running"
    }