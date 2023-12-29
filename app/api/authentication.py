#this is an example, needs to be done correctly
from fastapi import APIRouter, Response, status
from services.authentication import *
from api.api_models import Authentication

class Endpoints():

    router = APIRouter()

    @router.post("/login", tags = ["authentication"])
    def login(body : Authentication.login, response : Response):

        response = Services.login(body = body, response = response)
        return response


"""
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

#app = FastAPI()

# Secret key to sign the JWT
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Define the OAuth2PasswordBearer for handling authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# Function to create a JWT token
def create_jwt_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Function to decode the JWT token
def decode_jwt_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid credentials")


# Example login endpoint
@app.post("/token")
async def login_for_access_token(username: str, password: str):
    # Replace the following with your actual user authentication logic
    # For simplicity, we'll assume any username/password is valid
    user = {"sub": username}
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt_token(data=user, expires_delta=expires)
    return {"access_token": access_token, "token_type": "bearer"}


# Example protected endpoint that requires a valid JWT token
@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    payload = decode_jwt_token(token)
    return {"message": "This is a protected route", "user": payload}
"""