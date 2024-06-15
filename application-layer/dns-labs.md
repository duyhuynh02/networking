# 1. NSLOOKUP
1. Run nslookup to obtain the IP address of the web server for the Indian Institute of Technology in Bombay, India: www.iitb.ac.in. What is the IP address of www.iitb.ac.in
```sh
Non-authoritative answer:
Name:   www.iitb.ac.in
Address: 103.21.124.133
```
2. What is the IP address of the DNS server that provided the answer to your nslookup command in question 1 above?
```sh
Server:         10.255.255.254
Address:        10.255.255.254#53
```
3. Did the answer to your nslookup command in question 1 above come from an authoritative or non-authoritative server?
```sh
Authoritative server 
```
4. Use the nslookup command to determine the name of the authoritative name server for the iit.ac.in domain. What is that name? (If there are more than one authoritative servers, what is the name of the first authoritative server returned by nslookup)? If you had to find the IP address of that authoritative name server, how would you do so?
```sh
nslookup -type=NS iitb.ac.in
Authoritative answers can be found from:
dns1.iitb.ac.in internet address = 103.21.125.129
dns2.iitb.ac.in internet address = 103.21.126.129
dns3.iitb.ac.in internet address = 103.21.127.129
```

## 2. The DNS cache on your computer 
```sh
Windows: ipconfig /flushdns 
```

```sh
Linux: sudo systemd-resolve --flush-caches 

For v22.04 and later versions of Ubuntu Linux: sudo resolvectl flush-caches
```

## 3. Tracing DNS with Wireshark 
5. Locate the first DNS query message resolving the name gaia.cs.umass.edu. What is the packet number in the trace for the DNS query message? Is this query message sent over UDP or TCP?
```sh
322 - TCP
```
6. Now locate the corresponding DNS response to the initial DNS query. What is the packet number in the trace for the DNS response message? Is this response message received via UDP or TCP?
```sh
323 - TCP 
```
7. What is the destination port for the DNS query message? What is the source port of the DNS response message?
```sh
Destination port: 80
Source port: 53163
```
8. To what IP address is the DNS query message sent?
```sh
128.119.245.12
```
9. Examine the DNS query message. How many “questions” does this DNS message contain? How many “answers” answers does it contain?
```sh
1
and 0 
```
10. Examine the DNS response message to the initial query message. How many “questions” does this DNS message contain? How many “answers” answers does it contain?
```sh
1 
and 3 

```
11. The web page for the base file http://gaia.cs.umass.edu/kurose_ross/ references the image object http://gaia.cs.umass.edu/kurose_ross/header_graphic_book_8E_2.jpg , which, like the base webpage, is on gaia.cs.umass.edu. What is the packet number in the trace for the initial HTTP GET request for the base file http://gaia.cs.umass.edu/kurose_ross/? What is the packet number in the trace of the DNS query made to resolve gaia.cs.umass.edu so that this initial HTTP request can be sent to the gaia.cs.umass.edu IP address? What is the packet number in the trace of the received DNS response? What is the packet number in the trace for the HTTP GET request for the image object http://gaia.cs.umass.edu/kurose_ross/header_graphic_book_8E2.jpg? What is the packet number in the DNS query made to resolve gaia.cs.umass.edu so that this second HTTP request can be sent to the gaia.cs.umass.edu IP address? Discuss how DNS caching affects the answer to this last question.
```sh

```
12. What is the destination port for the DNS query message? What is the source port of the DNS response message?
```sh
Dst port: 53
Src port: 57837

```
13. To what IP address is the DNS query message sent? Is this the IP address of your default local DNS server?
```sh
75.75.75.75
```
14. Examine the DNS query message. What “Type” of DNS query is it? Does the query message contain any “answers”?
```sh
Type A
No
```
15. Examine the DNS response message to the query message. How many “questions” does this DNS response message contain? How many “answers”
```sh
1
1
```
