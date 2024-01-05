from fastapi import APIRouter, Response, status, Depends

from services.projects import *
from api.api_models import Projects

#auth
from fastapi.security import HTTPAuthorizationCredentials
from services.authentication import Services
from services.helper_authentication import JWT_handler
from settings import auth_schema

class Endpoint():

    router = APIRouter()

    #project

    @router.post("/project/project", tags = ["projects"])
    def add_project(body : Projects.add_project, response : Response, token : HTTPAuthorizationCredentials = Depends(auth_schema)): #Depends(JWT_handler.verify_jwt)

        claims : dict = JWT_handler.verify_jwt(token = token)
        Services.permission_handler(claims = claims, required_roles = [0])

        response = Write.project(body = body, response = response)
        return response

    @router.get("/project/project/all", tags = ["projects"])
    def get_projects():

        response = Read.projects()
        return response

    @router.get("/project/project/public")
    def get_public_projects():

        response = Read.public_projects()
        return response

    @router.put("/project/project", tags = ["projects"])
    def update_project(body: Projects.update_project, response : Response):

        response = Udpdate.project(body = body, response = response)
        return response

    @router.delete("/project/project", tags = ["projects"])
    def delete_project(body: Projects.delete_project, response: Response):

        response = Delete.project()
        return response