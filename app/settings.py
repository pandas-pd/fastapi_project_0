import os
#from fastapi.security import HTTPBearer

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
JWT_SECRET_KEY : str                        = "enter_key_here"
JWT_ALGORITHM : str                         = "HS256"
JWT_ENCODING : str                          = "utf-8"

JWT_NAME : str                              = "fastapi_project0_token"
JWT_SECURE : bool                           = False #can only be set to true, when https is implemented

#auth_schema                                 = HTTPBearer()

JWT_ISS : str                               = "www.sample_url.com"
JWT_ACCESS_TOKEN_EXPIRE_SECONDS : int       = 2592000 # == 30 days

#mailer settings (do not push to public repository)
EMAIL_SENDER : str            = "mail_adress"
EMAIL_PASSWORD : str          = "mail_login"

#other settings
TIME_ZONE : str         = None #not in use
LANGUAGE : str          = "EN" #not in use
VERSION : float         = 1.0
