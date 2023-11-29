import os

#pathing
db_url : str                    = "sqlite.db"
settings_dir : str              = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL : str              = "sqlite:///" + os.path.join(settings_dir, db_url)

#database file, add as dynamic path to minimize seutp errors
#DATABASE_URL = "sqlite:///sqlite.db"

#other settings
TIME_ZONE = None #not in use
LANGUAGE = "EN" #not in use