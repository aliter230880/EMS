import http.server 
import socketserver 
import urllib.request 
import json 
import datetime 
PORT=8888  
LOG='foreo_log.txt'  
class P(http.server.SimpleHTTPRequestHandler):  
def do_GET(self):self.p()  
def do_POST(self):self.p() 
