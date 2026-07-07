from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import *
from auth import *
from dependencies import get_current_user
router=APIRouter()
@router.post("/register",response_model=UserResponse)
def register(user:UserCreate,db:Session=Depends(get_db)):
 if db.query(User).filter(User.email==user.email).first(): raise HTTPException(400,"Email exists")
 u=User(username=user.username,email=user.email,password=hash_password(user.password));db.add(u);db.commit();db.refresh(u);return u
@router.post("/login",response_model=Token)
def login(user:UserLogin,db:Session=Depends(get_db)):
 u=db.query(User).filter(User.email==user.email).first()
 if not u or not verify_password(user.password,u.password): raise HTTPException(401,"Invalid credentials")
 return {"access_token":create_access_token({"sub":u.email}),"token_type":"bearer"}
@router.get("/me",response_model=UserResponse)
def me(current_user:User=Depends(get_current_user)): return current_user
