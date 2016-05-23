#!/usr/local/bin/python3

import os
import cgi
import argparse
import http.server
import cgitb


cgitb.enable()

def web_server(port):
    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    server_address = ("",port)
    handler.cgi_directories = ["/cgi-bin" ]
    httpd = server(server_address,handler)

    print("Starting web server with CGI support on port: {!s} ...".format(port))
    httpd.serve_forever()

if __name__=='__main__':
    parser = argparse.ArgumentParser(description= 'CGI Server')
    parser.add_argument('--port',action="store",dest="port",type=int,required=True)
    given_args = parser.parse_args()
    web_server(given_args.port)
    
