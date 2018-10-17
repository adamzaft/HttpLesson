from http.server import BaseHTTPRequestHandler, HTTPServer
import XmlParser
from multiprocessing import Process
import requests

class myHTTPRequstHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
            post_data = self.rfile.read(content_length)  # <--- Gets the data itself

            print(post_data)
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

def run_server():
    serverIP = XmlParser.serverIP()
    serverPORT = XmlParser.serverPORT()
    print('Server address is:', serverIP, ':', serverPORT)
    server_address = (serverIP, int(serverPORT))
    httpd = HTTPServer(server_address, myHTTPRequstHandler)
    print('~~~~~~~~~ Server is online - welcome to SKYNET~~~~~~~~~')
    httpd.serve_forever()

def run():
    print('Starting HttpServer..please hold..')
    while 1:
        cmd = input('input command (ex. Get index.html): ')
        cmd = cmd.split()

        if cmd[0] == 'exit':  # type exit to exit
            break
        elif cmd[0] =='yaniv':
            print('you are gay')


if __name__ == '__main__':
   # info('Starting')
    p1=Process(target=run_server)
    p1.start()
    p1.join()

    run()