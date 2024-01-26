from fastapi import FastAPI
from api import skills, enums, projects, users, authentication # Import your route modules
from fastapi.middleware.cors import CORSMiddleware
from db.base import engine
from db import base
import os
from settings import ORIGINS

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
    version         = "0.2",
)

#add CORS middleware (for whitelisting frontend App)
app.add_middleware(
    CORSMiddleware,
    allow_origins = ORIGINS,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

#include routes, add news to add to funcitonality
routes : list =[
    skills.Endpoint.router,
    enums.Endpoint.router,
    projects.Endpoint.router,
    users.Endpoint.router,
    authentication.Endpoints.router,
    #add new here
]

for route in routes:
    app.include_router(route)
