from fastapi import APIRouter, Response, status
from services.users import *
from api.api_models import Users

class Endpoint():

    router = APIRouter()

    #Users
    @router.post("/users/user", tags = ["user"])
    def add_user(body : Users.add_user, response : Response):

        response = Write.user(body = body, response = Response)
        return response

    #Roles