from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")




class User(BaseModel):
    id: int
    username: str
    password: str
    
users_db = []


def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password:str):
    for user in users_db:
        if user.username == username and verify_password(password, user.password):
            return user
    return None

@app.post("/register")
def register(user: User):
    user.password = get_password_hash(user.password)
    users_db.append(user)
    return {"message:", "User registered successfully"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm= Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/protected")
def read_protected(token: str = Depends(oauth2_scheme)):
        user = authenticate_user(token, token)
        if not user:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"message": "This is a protected route"}
 
        

    