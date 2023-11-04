"""
- Creation of the virtual environment
- Installation of the needed packages
- Creating the sqlite database
- Populating the sqlite database with the needed Enum values
"""

import os
from app.db.base import session
from app.db.models.enums import *
from app.settings import DATABASE_URL

class Setup():

    def main():

        #variables for setup
        venv_name : str             = "env"
        dirname, filename : str     = os.path.split(os.path.abspath(__file__))

        #setup
        Setup.create_venv(venv_name, dirname)

    def create_venv(venv_name : str, dirname : str):

        #


if __name__ == "__main__":
    Setup.main()