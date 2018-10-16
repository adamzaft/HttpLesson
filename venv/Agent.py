from http.server import BaseHTTPRequestHandler, HTTPServer
import http.client
import XmlParser


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
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, myHTTPRequstHandler)
    print('~~~~~~~~~ Server is online - welcome to SKYNET~~~~~~~~~')
    agentID =XmlParser.agentID()
    print(agentID)
    agentIP = XmlParser.agentIP()
    print(agentIP)
    agentPORT = XmlParser.agentPORT()
    print(agentPORT)
    serverIP = XmlParser.serverIP()
    print(serverIP)
    serverPORT = XmlParser.serverPORT()
    print(serverPORT)
    httpd.serve_forever()

    # Initialize server and start it, need to add read from configuration -> IP and PORT and ID


if __name__ == '__main__':
    run()
