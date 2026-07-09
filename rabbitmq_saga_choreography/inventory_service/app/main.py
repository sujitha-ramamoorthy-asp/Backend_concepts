import asyncio

from contextlib import asynccontextmanager

from fastapi import FastAPI

from .database import (
    Base,
    engine
)

from .consumer import start_consumer


Base.metadata.create_all(bind=engine)


@asynccontextmanager
async def lifespan(app: FastAPI):

    asyncio.create_task(
        start_consumer()
    )

    yield


app = FastAPI(
    title="Inventory Service",
    lifespan=lifespan
)


@app.get("/")
async def home():

    return {
        "message": "Inventory Service Running"
    }


@app.get("/health")
async def health():

    return {
        "status": "UP"
    }