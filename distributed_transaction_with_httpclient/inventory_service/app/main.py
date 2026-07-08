from fastapi import Depends
from fastapi import FastAPI
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import Base
from app.database import engine
from app.database import get_db

from app.schemas import InventoryRequest
from app.schemas import InventoryResponse

from app.service import InventoryService

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/reserve", response_model=InventoryResponse)
def reserve(request: InventoryRequest, db: Session = Depends(get_db)):

    try:

        return InventoryService.reserve(db, request)

    except Exception as ex:

        raise HTTPException(status_code=400, detail=str(ex))


@app.get("/inventory", response_model=list[InventoryResponse])
def inventory(db: Session = Depends(get_db)):

    return InventoryService.get_all(db)
