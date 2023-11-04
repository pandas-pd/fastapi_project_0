from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import DATABASE_URL

# Define the database file path
#database_file = 'sqlite.db'

# Create a SQLite database engine
engine = create_engine(DATABASE_URL, echo=True)  # 'echo=True' for debugging

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Define a declarative base class
Base = declarative_base()

#import models:
from db.models import skills, project_backlog

# Database setup
# Create the database and tables if they don't exist
Base.metadata.create_all(bind=engine)

"""
if test == False
# Define a class for your table
class YourTable(Base):
    __tablename__ = 'your_table_name'  # Replace with your table name
    
    # Define columns and their data types
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the table in the database
Base.metadata.create_all(engine)

# Optionally, commit the transaction and close the session
session.commit()
session.close()
"""