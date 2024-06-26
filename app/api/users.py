from fastapi import APIRouter, Response, status, Depends, Request
from services.users import *
from api.api_models import Users, Passwords

#auth
from services.authentication import Services
from services.helper_authentication import JWT_handler


class Endpoint():

    router = APIRouter()

    #Users
    @router.post("/users/validate_username", tags = ["user"])
    def validate_username(body: Users.validate_username, response : Response):

        response = Write.validate_username(body = body, response = response)
        return response

    @router.post("/users/user", tags = ["user"])
    def add_user(body : Users.add_user, response : Response):

        response = Write.user(body = body, response = response)
        return response

    @router.get("/users/all_users", tags = ["user"])
    def get_all_users(request : Request):

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [0])

        response = Read.all_users()
        return response

    @router.get("/users/user", tags = ["user"])
    def get_user(request : Request):

        claims = JWT_handler.verify_jwt(token = request.cookies)

        response = Read.user(key_user = claims["sub"])
        return response


    @router.put("/users/user", tags = ["user"])
    def update_user(body : Users.update_user, response : Response, request : Request):

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [], user_dependent = True, key_user = body.key) #This is an ID10T solution

        response = Update.user(body = body, response = response)
        return response

    @router.delete("/users/user", tags = ["user"])
    def delete_user(body : Users.delete_user, response : Response, request : Request):

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [], user_dependent = True, key_user = body.key) #This is an ID10T solution

        response = Delete.user(body = body, response = response)
        return response


    #Roles
    @router.post("/users/role", tags = ["role"])
    def add_role(body : Users.add_role, response : Response, request : Request):

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [0])

        response = Write.role(body = body, response = response)
        return response

    @router.get("/users/roles", tags = ["role"])
    def get_roles(key_user : int, response : Response, request : Request):

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [0])

        response = Read.roles(key_user = key_user, response = response)
        return response

    @router.delete("/users/role", tags = ["role"])
    def delete_role(body : Users.delete_role, response : Response, request : Request):

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [0])

        response = Delete.role(body = body, response = response)
        return response


    #password management
    @router.put("/users/password", tags = ["password"])
    def update_password(body : Passwords.update_password, response : Response, request : Request):

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [], user_dependent = True, key_user = body.key_user)

        response = Update.password(body = body, response = response)
        return response

    @router.post("/users/reset_password", tags = ["password"])
    def reset_password(body : Passwords.reset_password, response : Response):

        response = Update.reset_password(body = body, response = response)
        return response