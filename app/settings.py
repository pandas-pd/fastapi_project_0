import os

#pathing
db_url : str                    = "sqlite.db"
settings_dir : str              = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL : str              = "sqlite:///" + os.path.join(settings_dir, db_url)

#database file, add as dynamic path to minimize seutp errors
#DATABASE_URL = "sqlite:///sqlite.db"

#password settings
ENCODING  : str         = "utf-8"
SALT_ROUNDS : int       = 12

#other settings
TIME_ZONE : str         = None #not in use
LANGUAGE : str          = "EN" #not in use