# fastapi project 0 - Webapp: About me

# Frontend
The frontend runs on an NGINX server
Setup:
- Windows: https://medium.com/@chandramuthuraj/installing-nginx-on-windows-a-step-by-step-guide-6750575c63e2
- Linux: https://medium.com/@mayrain1923/setup-nginx-on-debian-12-and-host-a-simple-static-website-f832e6761e63


# Backend

## To be implemented
- Cookie Auth: https://indominusbyte.github.io/fastapi-jwt-auth/usage/jwt-in-cookies/
    - Current Auth: HTTP Bearer (only suitable for Webservices, vulnerable to XSS)
- Set https in prod env: https://medium.com/@mariovanrooij/adding-https-to-fastapi-ad5e0f9e084e
- GUI
    - Home page about the auother (me) with technical skills
    - Prject Backlog page
    - Role management

## About this app
- First try of a fullstack webapp with fastapi and a simple front end (to be implemented). This project serves as a strating point and a learning experience for the auther
- The App was developed with python 3.10. Thus python 3.10 or higher is reccomeded
- The `setup_env.py` and `setup_db.py` file needs to be run first for the app to funciton propperly. Could be replaced by an deployment pipeline. Automatically handles:
    - Creation of the virtual environment
    - Installation of the needed packages
    - Creating the sqlite database
    - Populating the sqlite database with the needed Enum values

### Notes to self
- If new default values likes enums should be added as a default to the database if not yet in exisitng, add the enum models and values to `setup.py`
- currently working on:
    - `setup.py`:
        - Implement a setup pipeline
        - Populate enum models
- post forwarding on yallo box: https://portforward.com/arris/tg3492lg-yl/
- mock-up guis: https://moqups.com/

## Setup
- run `setup_env.py`
- run `setup_db.py`
- create and overvrite the sample api key and secret in `settings.py`
- enter mailing server credentials in `settings.py`
- launch server

## Usefull commands:
- Activate and deactivate Environment on windows:
    - `.\env\Scripts\activate`
    - `deactivate`
- Launch API app:
    - `uvicorn main:app`
- Access documentation:
    - *webadress*/docs
    - *webadress*/redoc

# View Page
