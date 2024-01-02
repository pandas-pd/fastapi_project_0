from fastapi import APIRouter, Response, status, Depends
from services.projects import *
from api.api_models import Projects

from services.authentication import Services
from services.helper_authentication import JWT_handler

class Endpoint():


    router = APIRouter()

    #project

    @router.post("/project/project", tags = ["projects"])
    def add_project(body : Projects.add_project, response : Response, claims : str = Depends(JWT_handler.verify_jwt)):

        if (Services.permission_handler(response = response, claims = claims, required_roles = [0]) == False):
            return None

        response = Write.project(body = body, response = response)
        return response

    @router.get("/project/project", tags = ["projects"])
    def get_projects():

        response = Read.project()
        return response

    @router.put("/project/project", tags = ["projects"])
    def update_project(body: Projects.update_project, response : Response):

        response = Udpdate.project(body = body, response = response)
        return response

    @router.delete("/project/project", tags = ["projects"])
    def delete_project(body: Projects.delete_project, response: Response):

        response = Delete.project()
        return response