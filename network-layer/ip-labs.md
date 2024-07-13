# Labs - Wireshark 
If you're unable to run Wireshark on a live network connection or are answering question via an LMS (Learning Management System), you can download a packet trace file that was captured while following the steps above. 

Note: I'm currently using WSL so it could be different. 

## Part 1: Basic IPv4  
1. Select the first UDP segment sent by your computer via the traceroute command to gaia.cs.umass.edu. (Hint: this is 44th packet in the trace file in the ip-wireshark-trace1-1.pcapng file in footnote 2). Expand the Internet Protocol part of the packet in the packet details window. What is the IP address of your computer?
```sh
172.20.223.147 
```

2. What is the value in the time-to-live (TTL) field in this IPv4 datagram’s header?
```sh
1
```
3. What is the value in the upper layer protocol field in this IPv4 datagram’s header? [Note: the answers for Linux/MacOS differ from Windows here].
```sh
UDP (17)
```
4. How many bytes are in the IP header?
```sh
20 bytes
```
5. How many bytes are in the payload of the IP datagram? Explain how you determined the number of payload bytes.
```sh
56 bytes. 56 - 20 = 36 bytes
```
6. Has this IP datagram been fragmented? Explain how you determined whether or not the datagram has been fragmented
```sh
No
```
7. Which fields in the IP datagram always change from one datagram to the next within this series of UDP segments sent by your computer destined to 128.119.245.12, via traceroute? Why?
```sh
identification and checksum, obviously
```
8. Which fields in this sequence of IP datagrams (containing UDP segments) stay constant? Why?
```sh
The rest
```
9. Describe the pattern you see in the values in the Identification field of the IP datagrams being sent by your computer.
```sh
+1 sequence 
```

10. What is the upper layer protocol specified in the IP datagrams returned from the routers? [Note: the answers for Linux/MacOS differ from Windows here].
```sh
ICMP (1)
```

11. Are the values in the Identification fields (across the sequence of all of ICMP packets from all of the routers) similar in behavior to your answer to question 9 above?
```sh
Yes
```

12. Are the values of the TTL fields similar, across all of ICMP packets from all of the routers?
```sh
No, it's not the same at all.
```

## Part 2: Fragmentation
13. Find the first IP datagram containing the first part of the segment sent to 128.119.245.12 sent by your computer via the traceroute command to gaia.cs.umass.edu, after you specified that the traceroute packet length should be 3000. (Hint: This is packet 179 in the ip-wireshark-trace1-1.pcapng trace file in footnote 2. Packets 179, 180, and 181 are three IP datagrams created by fragmenting the first single 3000-byte UDP segment sent to 128.119.145.12). Has that segment been fragmented across more than one IP datagram? (Hint: the answer is yes4!)
```sh
Yes
```

14. What information in the IP header indicates that this datagram been fragmented?
```sh
More fragments?
```

15. What information in the IP header for this packet indicates whether this is the first fragment versus a latter fragment?
```sh
The flag is 1
```

16. How many bytes are there in is this IP datagram (header plus payload)?
```sh
1480 (+20 bytes header)
```

17. Now inspect the datagram containing the second fragment of the fragmented UDP segment. What information in the IP header indicates that this is not the first datagram fragment?
```sh
hmm i have no idea for this :) 
```

18. What fields change in the IP header between the first and second fragment?
```sh
Fragment offset and header checksum 
```

19. Now find the IP datagram containing the third fragment of the original UDP segment. What information in the IP header indicates that this is the last fragment of that segment
```sh
The flag for the last fragment is 0. 
```

## IPv6
20. What is the IPv6 address of the computer making the DNS AAAA request? This is the source address of the 20th packet in the trace. Give the IPv6 source address for this datagram in the exact same form as displayed in the Wireshark window5.
```sh
20	3.814489	2601:193:8302:4620:215c:f5ae:8b40:a27a	
```

21. What is the IPv6 destination address for this datagram? Give this IPv6 address in the exact same form as displayed in the Wireshark window.
```sh
2001:558:feed::1	
```

22. What is the value of the flow label for this datagram?
```sh
Flow Label: 0x63ed0
```

23. How much payload data is carried in this datagram?
```sh
37
```

24. What is the upper layer protocol to which this datagram’s payload will be delivered at the destination
```sh
ICMPv6 (on Windows)
```

25. How many IPv6 addresses are returned in the response to this AAAA request?
```sh
1 (?)
```

26. What is the first of the IPv6 addresses returned by the DNS for youtube.com (in the ip-wireshark-trace2-1.pcapng trace file, this is also the address that is numerically the smallest)? Give this IPv6 address in the exact same shorthand form as displayed in the Wireshark window
```sh

```