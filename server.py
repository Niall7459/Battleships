//Built off of HTTP Server module.
//WE can use to repsond from the battleships client.

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
        self._set_headers()
        self.wfile.write("Post")
        
def run(server_class=HTTPServer, handler_class=S, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting the http server...'
    httpd.serve_forever()

run()
