from http.server import BaseHTTPRequestHandler, HTTPServer
import XmlParser

class myHTTPRequstHandler(BaseHTTPRequestHandler):
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

    serverIP = XmlParser.serverIP()
    serverPORT = XmlParser.serverPORT()
    print('Server address is:',serverIP,':',serverPORT)
    server_address = (serverIP, int(serverPORT))
    httpd = HTTPServer(server_address, myHTTPRequstHandler)
    print('~~~~~~~~~ Server is online - welcome to SKYNET~~~~~~~~~')
    httpd.serve_forever()


if __name__ == '__main__':
    run()