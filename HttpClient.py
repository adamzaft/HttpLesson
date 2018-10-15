import sys
import http.client

# Get http server IP
http_server = sys.argv[1]
# Create a connection
conn = http.client.HTTPConnection(http_server)

while 1:
    cmd = input('input command (ex. Get index.html): ')
    cmd = cmd.split()

    if cmd[0]=='exit' : # type exit to exit
        break

    # Request command to server
    conn.request(cmd[0], cmd[1])

    # Get response from server
    rsp = conn.getresponse()

    # Print server response and data
    print(rsp.status, rsp.reason)
    data_received = rsp.read()
    print(data_received)

conn.close()
