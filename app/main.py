from fastapi import FastAPI
from api import skills, enums  # Import your route modules
from db.base import engine
from db import base
import os

#make all moduls accessable form everywhere
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#docu can be found under /docs#/default/
#load description
file = open("docu.md", "r")
description = file.read()

#instanciate app
app = FastAPI(
    title           = "Backend for webapp",
    description     = description,
    version         = "0.1",
)

#include routes, add news to add to funcitonality
routes : list =[
    skills.Endpoint.router,
    enums.Endpoint.router,
    #add new here
]

for route in routes:
    app.include_router(route)
