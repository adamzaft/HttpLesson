from http.server import BaseHTTPRequestHandler, HTTPServer
# import http.client
import XmlParser
import argparse
from multiprocessing import Process
import requests
import json

parser = argparse.ArgumentParser()
parser.add_argument("--agentid", help="Indicates agent ID")
args = parser.parse_args()

class myHTTPRequstHandler(BaseHTTPRequestHandler): # override POST command
    def do_POST(self):
        try:
            # send 200 response
            self.send_response(200)
            # send header first
            self.send_header('Content-type', 'text-html')
            self.end_headers()

            # send file content to client -> need to add logics HERE

            my_str = "Entering POST Section in server"
            my_str_as_bytes = str.encode(my_str)
            self.wfile.write(my_str_as_bytes)
        except IOError:
            self.send_error(404, 'Error from POST')



def run():
    print('Starting Agent..please hold..')
    agentIP = XmlParser.agentIP()
    print(agentIP)
    agentPORT = XmlParser.agentPORT()
    print(agentPORT)
    server_address = (agentIP, int(agentPORT))
    httpd = HTTPServer(server_address, myHTTPRequstHandler)
   # print('~~~~~~~~~ Agent',XmlParser.agentID(args.agentid),' is online - welcome to SKYNET~~~~~~~~~')
    print('~~~~~~~~~ Agent', XmlParser.agentID('1'), ' is online - welcome to SKYNET~~~~~~~~~')
    httpd.serve_forever()

    # Initialize server and start it, need to add read from configuration -> IP and PORT and ID

if __name__ == '__main__':

    #run()
    serverIP = XmlParser.serverIP()
    print('Server ip is:',serverIP)
    serverPORT = XmlParser.serverPORT()
    print('Server port is:',serverPORT)

    #conn = http.client.HTTPConnection(serverIP)


    #str_byte=str.encode('POST')
    #conn.send(str_byte)
    # Get response from server
    #rsp = conn.getresponse()
    # Print server response and data
   # print(rsp.status, rsp.reason)
    #data_received = rsp.read()
    #print(data_received)

    #conn.close()
    payload = {'some': 'data'}
    r= requests.post('http://127.0.0.1', data={'foo': 'bar'})
    print(r.text)