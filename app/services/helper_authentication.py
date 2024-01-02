from fastapi import FastAPI, Depends, HTTPException, status, Request
from jose import jws, JWSError
from datetime import datetime, timedelta
from typing import Optional
import time
import json


from settings import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES, JWT_ISS, JWT_ENCODING


class JWT_handler():

    @staticmethod
    def issue_jwt(key_user : int, key_roles : list) -> bytes:

        exp = int(time.time() + (JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60))

        claims : dict = {
            "iss"       : JWT_ISS,
            "exp"       : exp,
            "sub"       : key_user,
            "roles"     : key_roles,
        }

        jwt : str = jws.sign(
            payload = claims,
            key = JWT_SECRET_KEY,
            algorithm = JWT_ALGORITHM,
        )

        return jwt

    @staticmethod
    def verify_jwt(request : Request) -> dict:

        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid bearer",
            headers={"Authorization": "bearer"},
        )

        #get Auth header field with bearer
        bearer = request.headers.get("Authorization")

        #check integrety
        try:
            jwt_encoded = jws.verify(token = bearer, key = JWT_SECRET_KEY, algorithms = JWT_ALGORITHM)
        except:
            raise credentials_exception

        #check exp
        jwt_dict : dict = JWT_handler.decode_jwt(jwt_encoded, encrypted = False)
        exp = int(jwt_dict["exp"])

        if (exp < time.time()):
            raise credentials_exception

        return jwt_dict

    @staticmethod
    def decode_jwt(jwt_encoded, encrypted : bool) -> dict:

        if (encrypted == True):
            jwt_encoded = jws.verify(token = jwt_encoded, key = JWT_SECRET_KEY, algorithms = JWT_ALGORITHM)

        jws_decoded : str       = jwt_encoded.decode(JWT_ENCODING)
        jws_dict : dict         = json.loads(jws_decoded)

        return jws_dict