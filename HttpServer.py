from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import http.client


class ThreadedHTTPServer(object):
    def __init__(self,host,port, request_handler=BaseHTTPRequestHandler):
        server_address = (host, port)
        self.server = HTTPServer(server_address, myHTTPRequstHandler)
        print('~~~~~~~~~ Server is online - welcome to SKYNET~~~~~~~~~')
        self.server_thread=threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon=True

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def __start__(self):
        self.server_thread.start()

    def __stop__(self):
        self.server.shutdown()
        self.server.server_close()


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
   # server_address=('127.0.0.1', 80)
   # httpd = HTTPServer(server_address, myHTTPRequstHandler)
    #print('~~~~~~~~~ Server is online - welcome to SKYNET~~~~~~~~~')
    #httpd.serve_forever()

   # with ThreadedHTTPServer("localhost", 8000, request_handler=handler) as server:

    httpd = ThreadedHTTPServer('127.0.0.1',80,request_handler=myHTTPRequstHandler)

    httpd.server_thread.start()


if __name__ =='__main__':
    run()
http_server = '127.0.0.1'

# Create a connection
conn = http.client.HTTPConnection(http_server)
while 1:
    cmd = input('input command (ex. Get index.html): ')
    cmd = cmd.split()

    if cmd[0]=='exit' : # type exit to exit
        break

    # Request command to server
    if len(cmd)>1:
        conn.request(cmd[0], cmd[1])
    else:
        conn.request('POST',cmd[0])
    # Get response from server
    rsp = conn.getresponse()

    # Print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)

conn.close()
