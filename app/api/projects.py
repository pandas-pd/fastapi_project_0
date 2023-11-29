from fastapi import APIRouter, Response, status
from services.projects import *
from api.api_models import Projects

class Endpoint():

    router = APIRouter()

    #project

    @router.post("/add_project", tags = ["projects"])
    def add_project(body : Projects.add_project, response : Response):

        response = Write.project(body = body, response = response)
        return response

    @router.get("/get_projects", tags = ["projects"])
    def get_projects():

        response = Read.project()
        return response
