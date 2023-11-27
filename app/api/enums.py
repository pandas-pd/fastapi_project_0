from fastapi import APIRouter
from services.enums import *

class Endpoint():

    router = APIRouter()

    @router.get("/get_skill_levels", tags = ["enum"])
    def get_skill_levels():

        response = Read.skill_level()
        return response

    @router.get("/get_project_status", tags = ["enum"])
    def get_project_status():

        response = {"message" : "implement this you rice cracker"}
        return response