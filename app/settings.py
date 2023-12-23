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

#auth settings (do not push into public repository)
SECRET_KEY : str                        = "0MWV5n8wEKX1RCbKtX2PQoHzTuRneiTIPucuzYoVFWU7WKgL29AU0_59Xa_LkFGF"
ALGORITHM : str                         = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES : int       = 60 * 24 * 30 # 30 days

#other settings
TIME_ZONE : str         = None #not in use
LANGUAGE : str          = "EN" #not in use