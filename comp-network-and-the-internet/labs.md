# Labs - Wireshark 
If you're unable to run Wireshark on a live network connection or are answering question via an LMS (Learning Management System), you can download a packet trace file that was captured while following the steps above. 

# Answers 
1. Which of the following protocols are shown as appearing (i.e., are listed in the Wireshark “protocol” column) in your trace file: TCP, QUIC, HTTP, DNS, UDP, TLSv1.2?
```sh
TCP, DNS, UDP, TLSv1.2, SSL, IMCPv6
```

2. How long did it take from when the HTTP GET message was sent until the HTTP OK reply was received? (By default, the value of the Time column in the packet-listing window is the amount of time, in seconds, since Wireshark tracing began. (If you want to display the Time field in time-of-day format, select the Wireshark View pull down menu, then select Time Display Format, then select Time-of-day.)) 
```sh
Less than 0.2s 
```

3. What is the Internet address of the gaia.cs.umass.edu (also known as www-net.cs.umass.edu)? What is the Internet address of your computer or (if you are using the trace file) the computer that sent the HTTP GET message?
```sh
Source (my PC): 192.168.31.26 
Destionation (cs.umass.edu): 128.119.245.12 

Using tracefile:
$ tracert -h 4 www-net.cs.umass.edu

Tracing route to gaia.cs.umass.edu [128.119.245.12]
over a maximum of 4 hops:

  1     4 ms     3 ms     4 ms  XiaoQiang [192.168.31.1]
  2     5 ms     5 ms     5 ms  gpon.net [192.168.1.1]
  3    11 ms     6 ms     6 ms  10.204.0.2 [10.204.0.2]
  4     8 ms     7 ms     7 ms  172.16.0.96 [172.16.0.96]

I want to minimize the hops to 4, the destination still be 128.119.245.12 
```

4. Expand the information on the HTTP message in the Wireshark “Details of selected packet” window (see Figure 3 above) so you can see the fields in the HTTP GET request message. What type of Web browser issued the HTTP request? The answer is shown at the right end of the information following the “User-Agent:” field in the expanded HTTP message display. [This field value in the HTTP message is how a web server learns what type of browser you are using.]
```sh
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36\r\n
```
