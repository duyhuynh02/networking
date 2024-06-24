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

## Section 3.4
R9. In our rdt protocols, why did we need to introduce sequence numbers?
```sh
To know which packets we are sending successfully and lost packets. 
```

R10. In our rdt protocols, why did we need to introduce timers?
```sh
We need to resend the failed/ongoing packets in case it's lost or not receiving after a duration of time 
```

R11. Suppose that the roundtrip delay between sender and receiver is constant and known to the sender. Would a timer still be necessary in protocol rdt 3.0, assuming that packets can be lost? Explain.
```sh
Yes, it still be necessary. Knowing the RTT just help us how to put the approriate timer, not remove it completely. 
```

R12. Visit the Go-Back-N interactive animation at the Companion Website. 

a. Have the source send five packets, and then pause the animation before any of the five packets reach the destination. Then kill the first packet and resume the animation. Describe what happens.
```sh
The rest 4 packets still go the Receiver, but not retain any. Then after a duration, it remiding sending the first 5 packets, and this time the Receive get all. 
```
b. Repeat the experiment, but now let the first packet reach the destination and kill the first acknowledgment. Describe again what happens.
```sh
The rest 4 packets still go and this time Receive get all 4 packets and return back "ACK" to Sender. 
```
c. Finally, try sending six packets. What happens? 
```sh
Cannot be done, the window size limit to 5. 
```

R13. Repeat R12, but now with the Selective Repeat interactive animation. How are Selective Repeat and Go-Back-N different?
```sh
a) Receive still gets the 4 packets (and send the ACK!) even the first one is killed, then after a duraiton of time, the first one will be send again and also get the ACK. 

b) Same as Go-Back-N
c) Same 
```

## Section 3.5
R14. True or false?

a. Host A is sending Host B a large file over a TCP connection. Assume Host B has no data to send Host A. Host B will not send acknowledgments to Host A because Host B cannot piggyback the acknowledgments on data.
```sh
False 
```
b. The size of the TCP rwnd never changes throughout the duration of the connection.
```sh
False, it can change dynamically throughout the duration. 
```
c. Suppose Host A is sending Host B a large file over a TCP connection. The number of unacknowledged bytes that A sends cannot exceed the size of the receive buffer.
```sh
True 
```
d. Suppose Host A is sending a large file to Host B over a TCP connection. If the sequence number for a segment of this connection is m, then the sequence number for the subsequent segment will necessarily be m + 1.
```sh
True 
```
e. The TCP segment has a field in its header for rwnd.
```sh
True 
```
f. Suppose that the last SampleRTT in a TCP connection is equal to 1 sec. The current value of TimeoutInterval for the connection will necessarily be >= 1 sec.
```sh
True 
```
g. Suppose Host A sends one segment with sequence number 38 and 4 bytes of data over a TCP connection to Host
B. In this same segment, the acknowledgment number is necessarily 42.
```sh
True 
```

R15. Suppose Host A sends two TCP segments back to back to Host B over a TCP connection. The first segment has sequence number 90; the second has sequence number 110.
a. How much data is in the first segment?
```sh
20 
```
b. Suppose that the first segment is lost but the second segment arrives at B. In the acknowledgment that Host B sends to Host A, what will be the acknowledgment number?
```sh
110 
```
R16. Consider the Telnet example discussed in Section 3.5. A few seconds after the user types the letter ‘C,’ the user types the letter ‘R.’ After typing the letter ‘R,’ how many segments are sent, and what is put in the sequence number and acknowledgment fields of the segments?
```sh
2 segments are sent. 
Assume we have a segment number is A, then the segment number (sending 'R') will be A + 1 
```