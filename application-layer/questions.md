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
## Section 2.2 to 2.4
R10. What is meant by a handshaking protocol?
```sh
It's like an initlization, you want to say hello first before you can have a conversation. 
```

R11. What does a stateless protocol mean? Is IMAP stateless? What about SMTP?
```sh
Stateless means there is nothing to hold, everytime you send a new request, it won't be saved in the server. 

IMAP: Internet Message Access Protocol, use to pull mail from the receiver's mail server -> it's not stateless (stateful)

SMTP: Simple Mail Transfer Protocol, is a stateless protocol used for sending and receiving mail. 
```

R12. How can websites keep track of users? Do they always need to use cookies?
```sh
They use cookies. No, but cookie is the best method which easy to apply and use. 
Some others options are:
- First-party data 
- Device fingerprinting
- Third-party scripts 
```

R13. Describe how Web caching can reduce the delay in receiving a requested object. Will Web caching reduce the delay for all objects requested by a user or for only some of the objects? Why?
```sh
Setting up web caching near the "user geography". 

Web caching should be small due to physics, therefore there is a small of percentage of objects would be store (the most used ones). 
```

R14. Telnet into a Web server and send a multiline request message. Include in the request message the If-modified-since: header line to force a response message with the 304 Not Modified status code.
```sh
No idea. But if the question is this the object cached, then yes. 
```

R15. Are there any constraints on the format of the HTTP body? What about the email message body sent with SMTP? How can arbitrary data be transmitted over SMTP?
```sh
The data may contain 8-bit binary data
```

R16. Suppose Alice, with a Web-based e-mail account (such as Hotmail or Gmail),sends a message to Bob, who accesses his mail from his mail server using IMAP. Discuss how the message gets from Alice’s host to Bob’s host. Be sure to list the series of application-layer protocols that are used to move the message between the two hosts.
```sh
Alice and Bob both have their email server. Assume Alice sending email to Bob:
Alice ------(SMTP)---------> Alice's mail server
Alice's mail server -----(SMTP)-----> Bob's mail server 
Then Bob can use his email client (IMAP client) to connect, access and read the mail which Alice sent
```

R18. What is the HOL blocking issue in HTTP/1.1? How does HTTP/2 attempt to solve it?
```sh
HOL (Head-of-line) block occurs when too much parallel requests being sent. Subsequent requests must be wait before sending. 
In HTTP/2, we can simultaneously send many requests by request multiplexing 
```

R19. Why are MX records needed? Would it not be enough to use a CNAME record? (Assume the email client looks up email addresses through a Type A query and that the target host only runs an email server.)
```
MX records make sure the routing is correct while CNAME record provide aliasing capabilities. 
```

R20. What is the difference between recursive and iterative DNS queries?
```sh
Recursive query involve the local DNS server
Iterative query involve the DNS severs in the network 

For example, if you want to visit somewebsite.com: 
1. It will check the cache or the host file to see if there is a previous name solution 
2. If not found, your computer (DNS client) asks the local DNS server for the IP address recursively
3. If local still doesn't contain the record, it communicate with higher level DNS servers iteratively (root/TLD/etc...) 
4. When DNS server finds the resolved IP address, it replies to your client, and your browser stores it in memory for the future use 
```