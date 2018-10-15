import sys
import http.client

# Get http server IP from 1st cmd line
# http_server = sys.argv[1]

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
