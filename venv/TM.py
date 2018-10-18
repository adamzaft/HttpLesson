from http.server import BaseHTTPRequestHandler, HTTPServer
import XmlParser
from multiprocessing import Process
import requests
import threading


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

            my_str = "Received psot message at SERVER, sending response"
            my_str_as_bytes = str.encode(my_str)

            self.wfile.write(my_str_as_bytes)

        except IOError:
            self.send_error(404, 'Error from POST')


class ThreadedHTTPServer(object):
    def __init__(self,host,port, request_handler=myHTTPRequstHandler):
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

def run_server():
    serverIP = XmlParser.serverIP()
    serverPORT = XmlParser.serverPORT()
    print('Server address is:', serverIP, ':', serverPORT)
    server_address = (serverIP, int(serverPORT))
    httpd = ThreadedHTTPServer(serverIP,int(serverPORT),request_handler=myHTTPRequstHandler)
    print('~~~~~~~~~ Server is online - welcome to SKYNET~~~~~~~~~')
    httpd.server_thread.start()

def run():

    while 1:
        cmd = input('input command (ex. Get index.html): ')
        cmd = cmd.split()

        if cmd[0] == 'exit':  # type exit to exit
            break

        # Request command to server
        if cmd[0] == 'POST':
            try:
                server = 'http://' +XmlParser.agentIP()+':'+XmlParser.agentPORT()
                print(server)
                #server='http://127.0.0.1:81'
                print('sending to ip:', server)
                AgentPORT = XmlParser.agentPORT()
                print('Sending to port:', AgentPORT)
                payload = {'POST': 'SEND POST DATA FROM SERVER'}
                r = requests.post(server, json=payload)
                print(r.text)
            except IOError:
                print(IOError)
        if cmd[0] == 'GET':
            try:
                server = 'http://' + XmlParser.agentIP()
                print('Server ip is:', server)
                AgentPORT = XmlParser.agentPORT()
                print('Server port is:', AgentPORT)
                payload = {'some': 'data'}
                r = requests.get(server, json=payload)
                print(r.text)
            except IOError:
                print(IOError)

if __name__ == '__main__':

    run_server()
    run()