# PROBLEMS
I decide to work on problems which I found interesting and challenging. The full set of problems you can find and check on the textbook. Please buy a digital/hardcover to support the teachers. This solution is for educational purpose only.

## SOLUTIONS 
P1. True or false?
a. A user requests a Web page that consists of some text and three images. For this page, the client will send one request message and receive four response messages. 
```sh
False 
```
b. Two distinct Web pages (for example, www.mit.edu/research.html and www.mit.edu/students.html) can be sent over the same persistent connection.
```sh
True 
```

c. With nonpersistent connections between browser and origin server, it is possible for a single TCP segment to carry two distinct HTTP request messages.
```sh
False 
```

d. The Date: header in the HTTP response message indicates when the object in the response was last modified.
```sh
True 
```

e. HTTP response messages never have an empty message body
```sh
False 
```

P2. SMS, iMessage, Wechat, and WhatsApp are all smartphone real-time messaging systems. After doing some research on the Internet, for each of these systems write one paragraph about the protocols they use. Then write a paragraph explaining how they differ.
```sh
SMS: mobile telephony protocol / through cellular network 
iMessage: OTT application, use Internet Protocol
Whatsapp: Over The Top (OTT) application
```

P3. Assume you open a browser and enter http://yourbusiness.com/ about.html in the address bar. What happens until the webpage is displayed? Provide details about the protocol(s) used and a high-level description of the messages exchanged.
```sh
1. Browser take an url then parse it (based on the protocol, in this case, HTTP)
2. Then browser looks up the IP address assosiated with the domain name using DNS, DNS resolves the human-readable name to an IP address e.g., 198.168.1.1 
3. Use the HTTP protocol to initialize the TCP connection between client and server 
4. Server response with 200 (in case off success) to client 
5. Client send the request with path (/) and query needed 
6. Server send response 
7. Browser render the objects 
```

P6. Obtain the HTTP/1.1 specification (RFC 2616). Answer the following
questions:

d. Either a server or a client may close a transport connection between them if either one detects the connection has been idle for some time. Is it possible that one side starts closing a connection while the other side is transmitting data via this connection? Explain.
```sh
Yes, it's possible. The side initiating closure sends a TCP FIN (finish) segment to signal the end of communication while the other side still can tranmist data until it receives the FIN segment 
```

P7. Suppose within your Web browser, you click on a link to obtain a Web page. The IP address for the associated URL is not cached in your local host, so a DNS lookup is necessary to obtain the IP address. Suppose that n DNS servers are visited before your host receives the IP address from DNS; the successive visits incur an RTT of RTT1, . . . , RTTn. Further suppose that the Web page associated with the link contains exactly one object, consisting of a large amount of HTML text. Let RTT0 denote the RTT between the local host and the server containing the object. Assuming transmission duration of 0.002 * RTT0 of the object, how much time elapses from when the client clicks on the link until the client receives the object?
```sh
T = 0.002 * (RTT0) + 2 * RTT0 + (RTT1 + .... + RTTn)
```

P8. Consider Problem P7 again and assume RTT0 = RTT1 = RTT2 = . . .
RTTn = RTT, Furthermore, assume a new HTML file, small enough to have negligible transmission time, which references nine equally small objects on the same server. How much time elapses with
a. non-persistent HTTP with no parallel TCP connections?
b. non-persistent HTTP with the browser configured for 6 parallel connections?
c. persistent HTTP?
```
Since non-persistent HTTP only allows one object at a time, so: 
a -> T = n * (RTTn)
b -> T = n * RTTn / 6 
c -> T = Rtt0 (since Rtt0 = Rtt1 = ... = Rttn)
```

P9. Consider Figure 2.12, for which there is an institutional network connected to the Internet. Moreover, assume the access link has been upgraded to 54 Mbps, and the institutional LAN is upgraded to 10 Gbps. Suppose that the average object size is 1,600,000 bits and that the average request rate from the institution’s browsers to the origin servers is 24 requests per second. Also suppose that the amount of time it takes from when the router on the Internet side of the access link forwards an HTTP request until it receives the response is three seconds on average (see Section 2.2.5). Model the total average response time as the sum of the average access delay (that is, the delay from Internet router to institution router) and the average Internet delay. For the average access delay, use ∆/(1 - ∆b), where ∆ is the average time required to send an object over the access link and b is the arrival rate of objects to the access link.
```sh
access link: 54 Mbps 
inst LAN: 10 Gbps 
object size: 1,600,000 bits 
from ins's browsers -> origin servers: 24 requests / 1s 
time to take from router on the internet -> receive response: 3s 
 total average response = avereage access delay + avereage internet delay = ∆/(1 - ∆b) + 3s
```

a. Find the total average response time.
```sh
∆ = 1600000 / 54 * 10^6 = 0.0296s 
∆ = average time of the arrival rate of ojects = 0.0296 * 24 = 0.7104 
=> average time access delay = 0.0296 / (1 - 0.7184) = 0.1022s 
total average response = 0.1022s + 3s = 3.1022s 
```
b. Now suppose a cache is installed in the institutional LAN. Suppose the miss rate is 0.3. Find the total response time.
```sh
Total response time = 0.3 * (time from browser to full internet) + 0.7 * (time from browser to cache)

T(browser-to-internet) = 0.3 * 3.1022 + 0.7 * (1,600,000 / 10 * 10^9) = 0.93066 + 0.00016 = 0.93082 ~ 0.93 
```

P12. Write a simple TCP program for a server that accepts lines of input from a client and prints the lines onto the server’s standard output. (You can do this by modifying the TCPServer.py program in the text.) Compile and execute your program. On any other machine that contains a Web browser, set the proxy server in the browser to the host that is running your server program; also configure the port number appropriately. Your browser should now send its GET request messages to your server, and your server should display the messages on its standard output. Use this platform to determine whether your browser generates conditional GET messages for objects that are locally cached
```sh
Check p12.py 
```

P13. Consider sending over HTTP/2 a Web page that consists of one video file and three images. Suppose that the video clip is transported as 5000 frames, and each image captures four frames.
a. If all the video frames are sent first without interleaving, how many “frame times” are needed until all images are sent?
```sh
Time(without-interleaving) = Time(5000-frames-being-sent) + Time(images-being-sent)
```
b. If frames are interleaved, how many frame times are needed until all three
images are sent?
```sh
12
```
