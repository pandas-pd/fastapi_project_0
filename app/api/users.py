from fastapi import APIRouter, Response, status
from services.users import *
from api.api_models import Users, Passwords

#auth
from fastapi.security import HTTPAuthorizationCredentials
from services.authentication import Services
from services.helper_authentication import JWT_handler
from settings import auth_schema

class Endpoint():

    router = APIRouter()

    #Users
    @router.post("/users/user", tags = ["user"])
    def add_user(body : Users.add_user, response : Response):

        response = Write.user(body = body, response = response)
        return response

    @router.get("/users/user", tags = ["user"])
    def get_users():

        response = Read.user()
        return response

    @router.put("/users/user", tags = ["user"])
    def update_user(body : Users.update_user, response : Response):

        response = Update.user(body = body, response = response)
        return response

    @router.delete("/users/user", tags = ["user"])
    def delete_user(body : Users.delete_user, response : Response):

        response = Delete.user(body = body, response = response)
        return response


    #Roles
    @router.post("/users/role", tags = ["role"])
    def add_role(body : Users.add_role, response : Response):

        response = Write.role(body = body, response = response)
        return response

    @router.get("/users/roles", tags = ["role"])
    def get_roles(key_user : int, response : Response):

        response = Read.roles(key_user = key_user, response = response)
        return response

    @router.delete("/users/role", tags = ["role"])
    def delete_role(body : Users.delete_role, response : Response):

        response = Delete.role(body = body, response = response)
        return response


    #password management
    @router.put("/users/password", tags = ["password"])
    def update_password(body : Passwords.update_password, response : Response):

        response = Update.password(body = body, response = response)
        return response

    @router.post("/users/reset_password", tags = ["password"])
    def reset_password(body : Passwords.reset_password, response : Response):

        response = Update.reset_password(body = body, response = response)
        return response