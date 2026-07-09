import asyncio

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import (
    Base,
    engine
)

from .consumer import start_consumer


# Create tables
Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Start RabbitMQ Consumer
    asyncio.create_task(
        start_consumer()
    )

    yield


app = FastAPI(
    title="Payment Service",
    lifespan=lifespan
)


@app.get("/")
async def home():

    return {
        "message": "Payment Service Running"
    }


@app.get("/health")
async def health():

    return {
        "status": "UP"
    }