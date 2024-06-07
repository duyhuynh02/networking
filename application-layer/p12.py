from socket import * 

serverPort = 1200
host = '' 
serverSocket = socket(AF_INET, SOCK_STREAM) #SOCK_STREAM dùng để tạo stream socket, use TCP 
serverSocket.bind((host, serverPort))
serverSocket.listen(1)
print(f"The server is ready to receive at all {host}:{serverPort}")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connection from {addr}")
    #received data thì store tron sentence 
    sentence = connectionSocket.recv(1024).decode() #1024 là maximum bytes mà connectionSocket nhận trong 1 call
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()