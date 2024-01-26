import uvicorn
import logging
from settings import SSL_CERTFILE, SSL_KEYFILE, HOST, PORT, MODULE_NAME

print("booting server")

uvicorn.run(
    MODULE_NAME,
    host = HOST,
    port = PORT,
    #ssl_keyfile = SSL_KEYFILE,
    #ssl_certfile = SSL_CERTFILE
)