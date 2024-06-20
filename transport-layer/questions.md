# HOMEWORK QUESTIONS
Questions in the textbook. Decided to answer most of the questions here. 

## Section 3.1 to 3.3
R2. Consider a planet where everyone belongs to a family of six, every family lives in its own house, each house has a unique address, and each person in a given house has a unique name. Suppose this planet has a mail service that delivers letters from source house to destination house. The mail service requires that (1) the letter be in an envelope, and that (2) the address of the destination house (and nothing more) be clearly written on the envelope. Suppose each family has a delegate family member who collects and distributes letters for the other family members. The letters do not necessarily provide any indication of the recipients of the letters.

b. In your protocol, does the mail service ever have to open the envelope and examine the letter in order to provide its service?
```sh
No need to, as long as we have an address, we also have a delegate member to send to the right family member. 
```
R3. How is a UDP socket fully identified? What about a TCP socket? What is the difference between the full identification of both sockets?
```sh
With UDP: we only use the destination port number 
With TCP: We use 4 tuple including source and destination IP address, port number.
```
R4. Describe why an application developer might choose to run an application over UDP rather than TCP.
```sh
UDP: Not sure the data is not corruped or not
TCP: Reliable 
```
R5. Why is it that voice and video traffic is often sent over TCP rather than UDP in today’s Internet? (Hint: The answer we are looking for has nothing to do with TCP’s congestion-control mechanism.)
```sh
Reliability, also buffering and playback which help users can comeback and play as they want, also the firewall construction because the UDP is mostly blocked by firewalls 
```
R6. Is it possible for an application to enjoy reliable data transfer even when the application runs over UDP? If so, how?
```sh
Yes, over time computer scientist develop an UDP with to make sure the data transfer is reliable, some protocols like RUDP (Reliable UDP) or Enet or use applicaiton level mechanism with ACK acknowldgement. 
```

R7. Suppose a process in Host C has a UDP socket with port number 6789. Suppose both Host A and Host B each send a UDP segment to Host C with destination port number 6789. Will both of these segments be directed to the same socket at Host C? If so, how will the process at Host C know that these two segments originated from two different hosts?
```sh
Yes, by using demultiplexing, each UDP segments contain: source IP address (either host A/host B) and source port number 
```
R8. Suppose that a Web server runs in Host C on port 80. Suppose this Web server uses persistent connections, and is currently receiving requests from two different Hosts, A and B. Are all of the requests being sent through the same socket at Host C? If they are being passed through different sockets, do both of the sockets have port 80? Discuss and explain.
```sh
No, because when using persistent connections -> that means they connect over TCP. 
Yes, both can have port 80 but diff remote IP address and port numbers (it means use different sockets with respective senders)
```