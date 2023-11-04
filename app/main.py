from fastapi import FastAPI
from api import skills  # Import your route modules
from db.base import engine
from db import base

#docu can be found under /docs#/default/

#load description
file = open("docu.md", "r")
description = file.read()

#instanciate app
app = FastAPI(
    title           = "Backen for webapp",
    description     = description,
    version         = "0.1",
)

#include routes, add news to add to funcitonality
routes : list =[
    skills.Endpoint.router,
    #add new here
]

for route in routes:
    app.include_router(route)

app.include_router(skills.Endpoint.router)
#app.include_router(project_backlog.router)