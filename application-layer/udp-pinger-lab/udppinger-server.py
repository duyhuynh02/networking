import random 
from socket import * 

'''DO NOT MODIFY THIS FILE'''

# Create a UDP socket 
# Notice the use of SOCK_DGRAM for UDP packets 
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket 
serverSocket.bind(('localhost', 12000))
print("Server start here on port 12000")

while True:
    # Generate random number in the range of 0 to 10 
    rand = random.randint(0, 10)
    print("Waiting for the message...")
    # Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client 
    message = message.upper()
    # If rand is less is than 4, we consider the packet lose and do not response 
    if rand < 4:
        continue 
    serverSocket.sendto(message, address)
