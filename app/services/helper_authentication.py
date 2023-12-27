from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import Optional

from settings import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES


class JWT_handler():

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    # Function to create a JWT token
    @staticmethod
    def create_jwt_token(data: dict, expires_delta: timedelta):

        data : dict  = {
            "issuer"                : None,
            "user_key"              : None,
            "user_role"             : None,
            "expires"               : None,
        }

        #expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode = data.copy()
    
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})

        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm = JWT_ALGORITHM)

        return encoded_jwt


    # Function to decode the JWT token
    @staticmethod
    def decode_jwt_token(token: str):
        try:
            payload = jwt.decode(token, JWT_SECRET_KEY, algorithms = [JWT_ALGORITHM])
            return payload
        except JWTError:
            raise HTTPException(status_code=401, detail="Invalid credentials")



class Authentication_schema():

    pass