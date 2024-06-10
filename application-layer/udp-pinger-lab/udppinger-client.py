from socket import * 
import time 

'''
(1) send the ping message using UDP (Note: Unlike TCP, you do not need to establish a connection first, 
since UDP is a connectionless protocol.)
(2) print the response message from server, if any
(3) calculate and print the round trip time (RTT), in seconds, of each packet, if server responses
(4) otherwise, print “Request timed out”
'''


serverName = 'localhost'
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_DGRAM)

for i in range(1, 11):
    message = f"Ping {i} "
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    start_time = time.time() 
    try: 
        clientSocket.settimeout(1.0)
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        end_time = time.time() 
        print(modifiedMessage.decode() + str(end_time - start_time))
    except timeout: 
        print(f"Request {i} time out.")

clientSocket.close()

