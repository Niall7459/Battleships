#Built off of HTTP Server module.
#WE can use to repsond from the battleships client.

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("Get")

    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])#size
        post_data = self.rfile.read(content_length) #data
        
        data = {}

        for var in post_data.split("&"):
            name = var.split("=")[0]
            value = var.split("=")[1]
            data.append(name, value) #Lukily mr toombs had us a lesson on dictionarys!
        
        action = data.get("action")
        response = "Incomplete!"
        
        if action == "connect":
            #Request connection RETURN Success TRUE : FALSE
        else if action == "hit":
            #Hit coords RETURN Did the user guess right, TRUE : FALSE
        else:
            #Error
        
        self._set_headers()
        self.wfile.write(response)

def run(server_class=HTTPServer, handler_class=S, port=3001):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting the http server...'
    httpd.serve_forever()

run()
