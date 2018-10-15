from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class myHTTPRequstHandler(BaseHTTPRequestHandler):
    # override GET command
    def do_GET(self):
        rootdir = 'D:/Python/HttpTests/'  # file location
        try:
            if self.path.endswith('.html'):
                f = open(rootdir + self.path)  # opens requested file

                # send 200 response
                self.send_response(200)

                # send header first
                self.send_header('Content-type', 'text-html')
                self.end_headers()

                # send file content to client
                self.wfile.write(f.read())
                f.close()
                return
        except IOError:
            self.send_error(404, 'File not found')

    def do_POST(self):
        try:
            # send 200 response
            self.send_response(200)

            # send header first
            self.send_header('Content-type', 'text-html')
            self.end_headers()

            # send file content to client

            my_str = "Entering POST Section in server"
            my_str_as_bytes = str.encode(my_str)

            self.wfile.write(my_str_as_bytes)

        except IOError:
            self.send_error(404, 'Error from POST')

def run():
    print('Starting HttpServer..please hold..')

    # ip and port of server
    # by default http server port is 80
    server_address=('127.0.0.1', 80)
    httpd = HTTPServer(server_address, myHTTPRequstHandler)
    print('~~~~~~~~~ Server is online - welcome to SKYNET~~~~~~~~~')
    httpd.serve_forever()

if __name__ =='__main__':
    run()

