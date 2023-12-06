from fastapi import APIRouter, Response, status
from services.projects import *
from api.api_models import Projects

class Endpoint():

    router = APIRouter()

    #project

    @router.post("/project/project", tags = ["projects"])
    def add_project(body : Projects.add_project, response : Response):

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
