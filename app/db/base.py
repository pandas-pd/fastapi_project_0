from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

#needed to run the setup.py script for the models. Could all be packed into the setup_db.py but i am lazy
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from settings import DATABASE_URL
except:
    from app.settings import DATABASE_URL

# Create a SQLite database engine
engine = create_engine(DATABASE_URL, echo=True)  # 'echo=True' for debugging

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Define a declarative base class
Base = declarative_base()

#import models, add new here:
from db.models import skills
from db.models import projects
from db.models import enums
from db.models import users

# Database setup. Create the database and tables if they don't exist
Base.metadata.create_all(bind=engine)
