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

    @staticmethod
    @router.get("/users/user", tags = ["user"])
    def get_users():

        response = Read.user()
        return response

    @router.put("/users/user", tags = ["user"])
    def update_user(body : Users.update_user, response : Response):

        response = Update.user(body = body, response = Response)
        return response

    @router.put("users/password", tags = ["user"])
    def update_password(body : Users.update_password, response : Response):
        pass

    @router.delete("/users/user", tags = ["user"])
    def delete_user(body : Users.delete_user, response : Response):
        pass


    #Roles