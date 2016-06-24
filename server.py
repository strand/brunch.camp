import BaseHTTPServer
import SimpleHTTPServer

class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    error_message_format = '''
    custom error message
    '''

BaseHTTPServer.test(MyHandler, BaseHTTPServer.HTTPServer)
