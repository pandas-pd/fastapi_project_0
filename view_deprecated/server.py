import http.server
import socketserver
import ssl

import os
from os.path import dirname, abspath

#server settings
PORT            = 5000
DIRECTORY       = os.path.join(dirname(dirname(abspath(__file__))),"page")
CERTIFICATE     = "path to cert"
KEY             = "path to key"

#config of webserver
Handler             = http.server.SimpleHTTPRequestHandler
Handler.directory   = DIRECTORY

Handler.extensions_map={
    ".manifest": "text/cache-manifest",
    ".html":    "text/html",
    ".png":     "image/png",
    ".jpg":     "image/jpg",
    ".svg":     "image/svg+xml",
    ".css":     "text/css",
    ".js":      "application/x-javascript",
    ".json":    "application/json",
    ".xml":     "application/xml",
    "":         "application/octet-stream", 
}


httpd = socketserver.TCPServer(("", PORT), Handler)

#add this when cert is there
"""
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile=KEY,
    certfile=CERTIFICATE,
    server_side=True
)
"""

print(f"Serving at port: http://127.0.0.1:{PORT} \nServing contents from: {DIRECTORY}")
httpd.serve_forever()