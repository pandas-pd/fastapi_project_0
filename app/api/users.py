from fastapi import APIRouter, Response, status
from services.users import *
from api.api_models import Users

class Endpoint():

    router = APIRouter()

    # Programming Languages