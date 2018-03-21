#!/usr/bin/env python
#Steps for Python Handler:

#1.  Download Ngrok from: https://ngrok.com/download
#2.  Start ngrok with `./ngrok http 8080`
#3.  Run `python pythonResponder.py` 
#4.  Use the ngrok endpoint and input that in Dialogflow's webhook url.

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        input = json.loads(post_data)
        print "Request body: %s" %(input)
        # The ACTION name from the make_name Dialogflow intent, change this if needed
        NAME_ACTION = 'make.name' 
        #The parameters that are parsed from the make_name INTENT, change these if needed
        COLOR_ARGUMENT = 'color';
        NUMBER_ARGUMENT = 'number';
        #Only run method if action matches the action we are needing in Dialogflow
        if NAME_ACTION == input['result']['action']:
            print "Action Matched"
            self.send_response(200)
            self._set_headers()
            color = input['result']['parameters']['color']
            number = input['result']['parameters']['number']
            json_output = json.dumps({'speech': 'Alright, your silly name is %s %s! I hope you like it! See you next time.'%(color,number),
                'displayText': 'Alright, your silly name is %s %s! I hope you like it! See you next time.'%(color,number)})
            self.wfile.write(json_output)
        else:
            print "No action matching %s" %(NAME_ACTION)
            self.send_response(404)
            self._set_headers()

#Change port below to match port in your ngrok start command
def run(server_class=HTTPServer, handler_class=S, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()