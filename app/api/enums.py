from fastapi import APIRouter
from services.enums import *

class Endpoint():

    router = APIRouter()

    @router.get("/enum/skill_levels", tags = ["enum"])
    def get_skill_levels():

        response = Read.skill_level()
        return response

    @router.get("/enum/project_status", tags = ["enum"])
    def get_project_status():

        response = Read.project_status()
        return response

    @router.get("/enum/user_roles", tags = ["enum"])
    def get_user_roles():

        response = Read.user_roles()
        return response
