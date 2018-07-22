from http.server import HTTPServer, BaseHTTPRequestHandler

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        # Headers
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        # Body
        self.wfile.write('Hello, HTTP\n'.encode())


if __name__ == '__main__':
    server_address = ('', 8383)
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()