
'''
(1) Client will need to establish a TCP connection with a mail server (e.g., a Google mail server)
(2) dialogue with the mail server using SMTP protocol 
(3) send an e-mail message to a recepient via the mail server 
(4) close the TCP connection with the mail server 

'''
from socket import * 

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
quit ="QUIT\r\n"

# My email and password (kashdjaj12IJ3IMD@)
email = "something@gmail.com"
password = "something2@"

# Choose a mail server and call it mailserver 
mailserver = "smtp.gmail.com" 

# Create a socket called clientSocket and establish a TCP connection with mailserver 
google_serverport = 587         # for TLS, 25 and 465 is for SSL 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, google_serverport))
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response 
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv1)

if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send STARTTLS command first 
tlsCommand = "STARTTLS\r\n"
clientSocket.send(tlsCommand.encode())
recv0 = clientSocket.recv(1024).decode()
print("Message after STARTTLS command:", recv0)


# Send MAIL FROM command and print server response 
mailFromCommand = f'MAIL FROM:<{email}>\r\n'
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)

# Send RCPT TO command and print server response. 
rcptToCommand = f'RCPT TO:<{email}>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)

# Send DATA command and print server response 
dataCommand = f'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)


# Send message data 
clientSocket.send(msg.encode())
# Message ends with a single period.
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)

# Send QUIT command and get server response.
clientSocket.send(quit.encode())
# Message ends with a single period.
recv6 = clientSocket.recv(1024).decode()
print(recv6)

clientSocket.close()