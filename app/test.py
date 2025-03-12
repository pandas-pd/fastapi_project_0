import os

SSL_KEYFILE                                  = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cert", "localhost-key.pem")
SSL_CERTFILE                                 = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cert" ,"localhost.pem")

f = open(SSL_KEYFILE)
print(f.read())

