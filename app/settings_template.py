import os

#server seetings and params
SSL_KEYFILE                                  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cert", "localhost-key.pem")
SSL_CERTFILE                                 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cert" ,"localhost.pem")
SSL_PASSWORD                                 = None

HOST                                        = "localhost"
PORT                                        = 8080  # Default HTTPS port
MODULE_NAME                                 = "main:app" #name of main file (do not change)

#db pathing
db_url : str                                = "sqlite.db"
settings_dir : str                          = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL : str                          = "sqlite:///" + os.path.join(settings_dir, db_url)

#password settings
ENCODING  : str                             = "utf-8"
SALT_ROUNDS : int                           = 6

#JWT general settings (do not push into public repository)
JWT_SECRET_KEY : str                        = "enter_key_here"
JWT_ALGORITHM : str                         = "HS256"
JWT_ENCODING : str                          = "utf-8"
JWT_ISS : str                               = "localhost"
JWT_ACCESS_TOKEN_EXPIRE_SECONDS : int       = 3600*5 # == 30 days
JWT_NAME : str                              = "fastapi_project0_token"

JWT_SECURE : bool                           = True #set to true when ssl cert is installed
JWT_HTTPONLY : bool                         = True
JWT_SAMESITE: str                           = "None" #Strict, Lax, None

#whitelis for accessing the api, change for prod
ORIGINS                                      = [
    "https://localhost:4200",  # Angular frontend
    "https://127.0.0.1:4200", # If using HTTPS locally
]

 #add ip of webserver of web page to restrict access
#ORIGINS                                      = ["*"] #add ip of webserver of web page to restrict access


#JWT security settings (prevention to XSS, CSRF, XSSI)
"""
prod settings:
JWT_SECURE : bool                           = True #set to true when ssl cert is installed
JWT_HTTPONLY : bool                         = True
JWT_SAMESITE: str                           = "None" #Strict, Lax, None

dev settings:
JWT_SECURE : bool                           = False #set to true when ssl cert is installed
JWT_HTTPONLY : bool                         = True
JWT_SAMESITE: str                           = "Lax" #Strict, Lax, None

"""


#mailer settings (do not push to public repository)
EMAIL_SENDER : str                          = "enter_mail_adress_here"
EMAIL_PASSWORD : str                        = "enter_mail_password_here"

#other settings
VERSION : float                             = 1.0
TIME_ZONE : str                             = None #not in use
LANGUAGE : str                              = "EN" #not in use
