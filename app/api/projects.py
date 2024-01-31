from fastapi import APIRouter, Response, status, Request

from services.projects import *
from api.api_models import Projects

#auth
from services.authentication import Services
from services.helper_authentication import JWT_handler

class Endpoint():

    router = APIRouter()

    #project

    @router.post("/project/project", tags = ["projects"])
    def add_project(body : Projects.add_project, response : Response, request : Request): #Depends(JWT_handler.verify_jwt)

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [0,1])

        response = Write.project(body = body, response = response)
        return response

    @router.get("/project/project/all", tags = ["projects"])
    def get_projects(request : Request):

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [0,1])

        response = Read.projects()
        return response

    @router.get("/project/project/public", tags = ["projects"])
    def get_public_projects():

        response = Read.public_projects()
        return response

    @router.put("/project/project", tags = ["projects"])
    def update_project(body: Projects.update_project, response : Response, request : Request):

        claims : dict = JWT_handler.verify_jwt(token = request.cookies)
        Services.permission_handler(claims = claims, required_roles = [0,1])

        response = Udpdate.project(body = body, response = response)
        return response

    @router.delete("/project/project", tags = ["projects"])
    def delete_project(body: Projects.delete_project, response: Response, request : Request):

        claims : dict = JWT_handler.verify_jwt(token =  request.cookies)
        Services.permission_handler(claims = claims, required_roles = [0,1])

        response = Delete.project()
        return response