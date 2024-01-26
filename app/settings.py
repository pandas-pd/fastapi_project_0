import os

#server seetings and params
SSL_KEYFILE                                 = "path_to_your_ssl_keyfile.key"
SSL_CERTFILE                                = "path_to_your_ssl_certfile.crt"

HOST                                        = "127.0.0.1"
PORT                                        = 8080  # Default HTTPS port
MODULE_NAME                                 = "main:app" #name of main file (do not change)

#whitelis for accessing the api, change for prod
ORIGINS                                      = ["*"] #add ip of webserver of web page to restrict access

#db pathing
db_url : str                                = "sqlite.db"
settings_dir : str                          = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL : str                          = "sqlite:///" + os.path.join(settings_dir, db_url)

#password settings
ENCODING  : str                             = "utf-8"
SALT_ROUNDS : int                           = 12

#JWT general settings (do not push into public repository)
JWT_SECRET_KEY : str                        = "enter_key_here"
JWT_ALGORITHM : str                         = "HS256"
JWT_ENCODING : str                          = "utf-8"
JWT_ISS : str                               = "www.sample_url.com"
JWT_ACCESS_TOKEN_EXPIRE_SECONDS : int       = 2592000 # == 30 days
JWT_NAME : str                              = "fastapi_project0_token"

#JWT security settings (prevention to XSS, CSRF, XSSI)
JWT_SECURE : bool                           = True #set to true when ssl cert is installed
JWT_HTTPONLY : bool                         = True
JWT_SAMESITE: str                           = "strict"

#mailer settings (do not push to public repository)
EMAIL_SENDER : str                          = "mail_adress"
EMAIL_PASSWORD : str                        = "mail_login"

#other settings
VERSION : float         = 1.0
TIME_ZONE : str         = None #not in use
LANGUAGE : str          = "EN" #not in use
