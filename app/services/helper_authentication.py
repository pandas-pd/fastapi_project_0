from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jws, JWSError
from datetime import datetime, timedelta
from typing import Optional
import time
import json

from settings import JWT_SECRET_KEY, JWT_ALGORITHM, JWT_ACCESS_TOKEN_EXPIRE_MINUTES, JWT_ISS


class JWT_handler():

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
    def verify_jwt(jwt : bytes) -> bool:

        #check integrety
        try:
            jwt_encoded = jws.verify(token = jwt, key = JWT_SECRET_KEY, algorithms = JWT_ALGORITHM)
        except JWSError:
            return False

        #check exp
        jwt_dict : dict = JWT_handler.decode_jwt(jwt_encoded, encrypted = False)
        exp = int(jwt_dict["exp"])

        if exp < time.time():
            return False

        return True

    @staticmethod
    def decode_jwt(jwt_encoded, encrypted : bool) -> dict:

        if (encrypted):
            jwt_encoded = jws.verify(token = jwt_encoded, key = JWT_SECRET_KEY, algorithms = JWT_ALGORITHM)

        jws_decoded : str       = jwt_encoded.decode("utf-8")
        jws_dict : dict         = json.loads(jws_decoded)

        return jws_dict



class Authentication_schema():

    pass