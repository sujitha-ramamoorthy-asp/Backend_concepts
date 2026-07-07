from datetime import datetime,timedelta
from jose import jwt,JWTError
from passlib.context import CryptContext
from dotenv import load_dotenv
import os
load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY");ALGORITHM=os.getenv("ALGORITHM");EXP=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
pwd=CryptContext(schemes=["bcrypt"],deprecated="auto")
hash_password=pwd.hash
verify_password=lambda p,h: pwd.verify(p,h)
def create_access_token(data):
 d=data.copy();d["exp"]=datetime.utcnow()+timedelta(minutes=EXP);return jwt.encode(d,SECRET_KEY,algorithm=ALGORITHM)
def verify_token(t):
 try:return jwt.decode(t,SECRET_KEY,algorithms=[ALGORITHM])
 except JWTError:return None
