from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from auth import verify_token
from models import User
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token:str=Depends(oauth2_scheme),db:Session=Depends(get_db)):
 p=verify_token(token)
 if not p: raise HTTPException(401,"Invalid Token")
 u=db.query(User).filter(User.email==p.get("sub")).first()
 if not u: raise HTTPException(401,"User not found")
 return u
