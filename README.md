# fastapi project 0 - Webapp: About me

## About this app
- First try of a fullstack webapp with fastapi an react. This project serves as a strating point and a learning experience for the auother
- The App was developed with python 3.10. Thus python 3.10 or higher is reccomeded
- The `setup.py` file needs to be run first for the app to funciton propperly. Could be replaced by an deployment pipeline. Automatically handles:
    - Creation of the virtual environment
    - Installation of the needed packages
    - Creating the sqlite database
    - Populating the sqlite database with the needed Enum values

### On the database
- If new default values likes enums should be added as a default to the database if not yet in exisitng, add the enum models and values to `setup.py`

## Usefull commands:

- Activate and deactivate Environment on windows:
    - `.\env\Scripts\activate`
    - `deactivate`
- Launch API app:
    - `uvicorn main:app`
- Access documentation:
    - *webadress*/docs
    - *webadress*/redoc

## To be implemented
- REST API
    - Technical Skills (Programming languaes)
    - Project Backlog with GitHub link

- GUI
    - Home page about the auother (me) with technical skills
    - Prject Backlog paget