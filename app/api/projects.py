from fastapi import APIRouter, Response, status
from services. import *
from api.api_models import Projects 

class Endpoint():

    router = APIRouter()

    #project

    @router.post("/add_project", tags = ["projects"])
    def add_project(body = Projects.add_project, response = Response):

        response = 
