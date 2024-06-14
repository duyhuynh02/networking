'''
Develop a small web proxy that is able to cache web pages, handle all kinds of objects: HTML, images,...

Client ---(request)----> Proxy server ---(request)----> Web server 
Client <--(response)---- Proxy server <--(response)---- Web server 
'''

from socket import * 
import sys 

if len(sys.argv) <= 1:
    print('Usage: "python3 proxy-server.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server]')
    sys.exit(2)

# Create a server socket, bind it to a port and start listening 
tcpSerSock = socket(AF_INET, SOCK_STREAM)

# Fill in start 
server_port = 8888
host = sys.argv[1]
tcpSerSock.bind((host, server_port)) 
tcpSerSock.listen(1)
print(f"The TCP server socket is ready to receive at {host}:{server_port}")

while 1: 
    # Start receiving data from the client 
    print('Ready to server...')
    tcpCliSock, addr = tcpSerSock.accept() 
    print('Received a connection from:', addr)
    message = tcpCliSock.recv(1024).decode()
    # Extract the filename from the given message 
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist = "false"
    filetouse = "/" + filename 
    print(filetouse)
    try:
        #Check whether the file exist in the cache 
        f = open(filetouse[1:], "r")
        outputdata = f.readlines()
        fileExist = "true"
        # ProxyServer finds a cache hit and generates a response message 
        tcpCliSock.send("HTTP/1.0 200 OK\r\n".encode())
        tcpCliSock.send("Content-Type:text/html\r\n".encode())

        for data in outputdata:
            tcpCliSock.send(data.encode())
        tcpCliSock.send("\r\n".encode())
        f.close()
        print('Read from cache')
    except IOError:
        if fileExist == "false":
            # Create a socket on the proxyserver 
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.", "", 1)
            print('HOSTN: ', hostn)
            try:
                # Connect to the socket to port 80 
                c.connect((hostn, 80))
                # Create a temporary file on this socket and ask port 80 for the file requested by the client 
                fileobj = c.makefile('rwb', 0)
                request = f"GET /{filename} HTTP/1.0\r\nHost: {hostn}\r\n\r\n"
                fileobj.write(request.encode())
                fileobj.flush()  #to make sure all the data is sent 
                # Read the response into buffer 
                buffer = fileobj.readlines()
                print(f"buffer: {buffer}")

                # Create a new file in the cache for the requested file 
                # Also send the response in the buffer to client socket and the corresponding file in the cache 
                tmpFile = open("./" + filename, "wb")
                for data in buffer:
                    tmpFile.write(data.encode())
                    tcpCliSock.send(data.encode())

                tmpFile.close()
            except: 
                print("Illegal request")

        else:
            # HTTP response message for file not found 
            tcpCliSock.send("HTTP/1.0 404 Not Found\r\n".encode())
            tcpCliSock.send("<html><body><h1>Error 404: Page not found</h1></body></html>".encode())
            # Close the client and the server sockets 
            tcpCliSock.close()