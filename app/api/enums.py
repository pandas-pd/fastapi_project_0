from fastapi import APIRouter
from services.enums import *

class Endpoint():

    router = APIRouter()

    @router.get("/get_skill_levels")
    def get_skill_levels():

        response = Read.skill_level()

        return response