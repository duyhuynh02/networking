# HOMEWORK QUESTIONS
Questions in the textbook. Decided to answer most of the questions here. 

## Section 2.1 
R1. List five nonproprietary Internet applications and the application-layer protocols that they use.
```sh
Web browsing - HTTP 
Email - SMTP 
Video streaming/games  
File transfer - FTP or SFTP 
DNS  
Remote Access - SSH/RDP/VNC 
```

R2. What is the difference between network architecture and application architecture?
```sh
Network architecture is a component of many applications and networks (like routers, switches, cable, protocols, host, destination,...)
Application architecture is a component of many parts of applications. (Uber, Netflix,...)
```

R3. For a communication session between a pair of processes, which process is the client and which is the server?
```sh
Client is the one who sends the request, server on the otherhand, active 24/7 and return the responses. 
```

R4. Why are the terms client and server still used in peer-to-peer applications?
```sh
I don't know. Maybe it's more familiar with people? Or do you want to call it as master-slave, jeez.... 
```

R5. What information is used by a process running on one host to identify a process running on another host?
```sh
1. IP address of the destination host.
2. Port 
```

R6. What is the role of HTTP in a network application? What other components are needed to complete a Web application?
```sh
HTTP stands for HyperText Transfer Protocol. It used to show to the human plain-based text as readable as possible. 

Other components:
- Backend programming
- Database 
- User Interface 
- Frontend programming 
- Security
- ... 
```

R7. Referring to Figure 2.4, we see that none of the applications listed in Figure 2.4 requires both no data loss and timing. Can you conceive of an application that requires no data loss and that is also highly time-sensitive?
```sh
Could be something related to human life? 
According to google, there is one application which not only requires no data loss, this is also highly time-sensitive is High-Querncy Trading (HFT) 
```

R8. List the four broad classes of services that a transport protocol can provide. For each of the service classes, indicate if either UDP or TCP (or both) provides such a service.
```sh
Reliable data transfer: TCP 
Throughput guarantee: None 
Timing guarantee: None 
Security: None (but TCP can be enhanced with SSL/TLS)
```

R9. Recall that TCP can be enhanced with TLS to provide process-to-process security services, including encryption. Does TLS operate at the transport layer or the application layer? If the application developer wants TCP to be enhanced with TLS, what does the developer have to do?
```sh
TLS should be on the transport layer. 
Maybe create a socket between 2 layers? 
```
