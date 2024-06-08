''' Develop a web server that handles one HTTP request at a time. Your web server should accept
and parse the HTTP request, get the requested file from the server’s file system, create an HTTP response
message consisting of the requested file preceded by header lines, and then send the response directly to
the client. If the requested file is not present in the server, the server should send an HTTP “404 Not
Found” message back to the client.
'''
from socket import * 
import sys 

#Prepare a server socket 
serverPort = 6789 
host = '192.168.31.26'
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((host, serverPort))
serverSocket.listen(1)
print(f"The server is ready to receive at {host}:{serverPort}")

while True:
    print('Ready to server...')
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        with open(filename[1:], 'r') as f: 
            print('hello world')
            outputdata = f.read() 

        #Send one HTTP header line into socket 
        header = 'HTTP/1.1 200 OK\n\n'
        connectionSocket.send(header.encode())
        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        #Send response message for file not found 
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><h1>Error 404: File not found</h1></body></html>'
        connectionSocket.send(header.encode())
        connectionSocket.send(response.encode())
        connectionSocket.close()

serverSocket.close()
sys.exit() #Termintate the program after sending the corresponding data 


''' Optional exercise

1. Currently, the web server handles only one HTTP request at a time. Implement a multithreaded server
that is capable of serving multiple requests simultaneously. Using threading, first create a main thread
in which your modified server listens for clients at a fixed port. When it receives a TCP connection
request from a client, it will set up the TCP connection through another port and services the client
request in a separate thread. There will be a separate TCP connection in a separate thread for each
request/response pair.

2. Instead of using a browser, write your own HTTP client to test your server. Your client will connect
to the server using a TCP connection, send an HTTP request to the server, and display the server
response as an output. You can assume that the HTTP request sent is a GET method.
The client should take command line arguments specifying the server IP address or host name, the
port at which the server is listening, and the path at which the requested object is stored at the server.
The following is an input command format to run the client.
client.py server_host server_port filename

'''