# Labs - Wireshark 
If you're unable to run Wireshark on a live network connection or are answering question via an LMS (Learning Management System), you can download a packet trace file that was captured while following the steps above. 

## Capturing and analyzing Ethernet frames 
1.	What is the 48-bit Ethernet address of your computer?
```sh
128.119.247.66 
```
2.	What is the 48-bit destination address in the Ethernet frame?  Is this the Ethernet address of gaia.cs.umass.edu? (Hint: the answer is no).  What device has this as its Ethernet address? [Note: this is an important question, and one that students sometimes get wrong.  Re-read pages 483-484 in the text and make sure you understand the answer here.]
```sh
128.119.245.12 
```
3. What is the hexadecimal value for the two-byte Frame type field in the Ethernet frame carrying the HTTP GET request? What upper layer protocol does this correspond to?
```sh
Type: IPv4 (0x0800) 
IP
```
4. How many bytes from the very start of the Ethernet frame does the ASCII “G” in “GET” appear in the Ethernet frame? Do not count any preamble bits in your count, i.e., assume that the Ethernet frame begins with the Ethernet frame's destination address.
```sh
N/A
```
5. What is the value of the Ethernet source address? Is this the address of your computer, or of gaia.cs.umass.edu (Hint: the answer is no). What device has this as its Ethernet address?
```sh
c4:41:1e:75:b1:52
```
6. What is the destination address in the Ethernet frame? Is this the Ethernet address of your computer?
```sh
00:1e:c1:7e:d9:01 (3ComEurope_7e:d9:01)
```
7. Give the hexadecimal value for the two-byte Frame type field. What upper layer protocol does this correspond to?
```sh
N/A
```
8. How many bytes from the very start of the Ethernet frame does the ASCII “O” in “OK” (i.e., the HTTP response code) appear in the Ethernet frame? Do not count any preamble bits in your count, i.e., assume that the Ethernet frame begins with the Ethernet frame's destination address.
```sh
N/A
```
9. How many Ethernet frames (each containing an IP datagram, each containing a TCP segment) carry data that is part of the complete HTTP “OK 200 ...” reply message?
```sh
Um 1? 
```

## The Address Resolution Protocol 
10. How many entries are stored in your ARP cache?
```sh
23 
```
11. What is contained in each displayed entry of the ARP cache
```sh
Internet address | Physical address | Type
```

12. What is the hexadecimal value of the source address in the Ethernet frame containing the ARP request message sent out by your computer?
```sh
check #5 
```
13. What is the hexadecimal value of the destination addresses in the Ethernet frame containing the ARP request message sent out by your computer? And what device(if any) corresponds to that address (e.g,, client, server, router, switch or otherwise...)?
```sh
check #6
```
14. What is the hexadecimal value for the two-byte Ethernet Frame type field. What upper layer protocol does this correspond to?
```sh
0x0806
```

15. How many bytes from the very beginning of the Ethernet frame does the ARP opcode field begin?
```sh
60 bytes 
```

16. What is the value of the opcode field within the ARP request message sent by your computer?
```sh
Opcode: request (1)
```

17. Does the ARP request message contain the IP address of the sender? If the answer is yes, what is that value?
```sh
Yes, 128.119.247.1
```

18. What is the IP address of the device whose corresponding Ethernet address is being requested in the ARP request message sent by your computer?
```sh
128.119.247.115
```

19. What is the value of the opcode field within the ARP reply message received by your computer?
```sh
request (1)
```

20. Finally (!), let’s look at the answer to the ARP request message! What is the Ethernet address corresponding to the IP address that was specified in the ARP request message sent by your computer (see question 18)?
```sh
host: 128.119.247.79 and dest: 169.254.1.0
```