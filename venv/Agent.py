from http.server import BaseHTTPRequestHandler, HTTPServer
import XmlParser
import argparse
from multiprocessing import Process
import requests
import json
import pytest
import threading

parser = argparse.ArgumentParser()
parser.add_argument("--agentid", help="Indicates agent ID")
args = parser.parse_args()




class myHTTPRequstHandlerAgent(BaseHTTPRequestHandler): # override POST command
    def do_POST(self):
        try:
            # send 200 response
            self.send_response(200)
            # send header first
            self.send_header('Content-type', 'text-html')
            self.end_headers()

            # send file content to client -> need to add logics HERE

            my_str = "Received POST message at AGENT, sending response"
            my_str_as_bytes = str.encode(my_str)
            self.wfile.write(my_str_as_bytes)
        except IOError:
            self.send_error(404, 'Error from POST')



class ThreadedHTTPServer(object):
    def __init__(self,host,port, request_handler=myHTTPRequstHandlerAgent):
        server_address = (host, port)
        self.server = HTTPServer(server_address, myHTTPRequstHandlerAgent)
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


def run():
    print('Starting Agent..please hold..')
    agentIP = XmlParser.agentIP()
    print(agentIP)
    agentPORT = XmlParser.agentPORT()
    print(agentPORT)
    server_address = (agentIP, int(agentPORT))
    # httpd = HTTPServer(server_address, myHTTPRequstHandler)
    httpd = ThreadedHTTPServer(agentIP,int(agentPORT),request_handler=myHTTPRequstHandlerAgent)
    # print('~~~~~~~~~ Agent',XmlParser.agentID(args.agentid),' is online - welcome to SKYNET~~~~~~~~~')
    print('~~~~~~~~~ Agent', XmlParser.agentID('1'), ' is online - welcome to SKYNET~~~~~~~~~')
    httpd.server_thread.start()

if __name__ == '__main__':

    run()

    while 1:
        cmd = input('input command (ex. Get index.html): ')
        cmd = cmd.split()

        if cmd[0] == 'exit':  # type exit to exit
            break


        # Request command to server
        if cmd[0]=='POST':
            try:
                server = 'http://' + XmlParser.serverIP()
                print('Sending to IP:', server)
                serverPORT = XmlParser.serverPORT()
                print('Sending to PORT:', serverPORT)
                payload = {'POST': 'SEND POST DATA FROM AGENT'}
                r = requests.post(server, json=payload)
                print(r.text)
            except IOError:
                print(IOError)


        if cmd[0]=='GET':
            try:
                server = 'http://' + XmlParser.serverIP()
                print('Server ip is:', server)
                serverPORT = XmlParser.serverPORT()
                print('Server port is:', serverPORT)
                payload = {'some': 'data'}
                r = requests.get(server, json=payload)
                print(r.text)
            except IOError:
                print(IOError)



    # sends pytest from execution --> need to so how to implement a set of tests
    # pytest.main(['-x','C:/Users/adamz/PycharmProjects/HttpLesson/venv/pytest_sample.py'])
    # pytest.cmdline.main(args)