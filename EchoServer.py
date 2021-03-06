from http.server import HTTPServer, BaseHTTPRequestHandler

class EchoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        # Headers
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        # Body
        self.wfile.write(self.path[1:].encode())


if __name__ == '__main__':
    server_address = ('', 8383)
    httpd = HTTPServer(server_address, EchoHandler)
    httpd.serve_forever()