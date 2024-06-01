# PROBLEMS
I decide to work on problems which I found interesting and challenging. The full set of problems you can find and check on the textbook. Please buy a digital/hardcover to support the teachers. This solution is for educational purpose only.

## SOLUTIONS 
P2. Equation 1.1 gives a formula for the end-to-end delay of sending one packet
of length L over N links of transmission rate R. Generalize this formula for
sending P such packets back-to-back over the N links
```sh
Equation 1.1: d(end-to-end) = N * L / R
=> Total time to send P packets: P * N * L / R 
```

P3. Consider an application that transmits data at a steady rate (for example, the sender generates an N-bit unit of data every k time units, where k is small and fixed). Also, when such an application starts, it will continue running for a relatively long period of time. Answer the following questions, briefly justifying your answer:
a. Would a packet-switched network or a circuit-switched network be more appropriate for this application? Why?
```sh
Packet-switched network: efficient use of bandwidth, flexible, scalable, lower cost 
Circuit-switched network: guranteed bandwidth, low latency, predictable performance, suitable for real-time communication

Based on two characterisitcs, we can see that with N-bit unit of data every k time units, packet-switchied network would be more suitable. 
```

b. Suppose that a packet-switched network is used and the only traffic in this network comes from such applications as described above. Furthermore, assume that the sum of the application data rates is less than the capacities of each and every link. Is some form of congestion control needed? Why?
```sh
Based on the definition, congestion control is the technique which can prevent the congestion. Congestion can cause a network response time slows down, and the delay increases, leading to retranmissions and worsening the situation. 

It will base on how much it's lesser. If it's lesser just a little bit (or equal just like we see the animation in the course), we still need some forms of congestion control. 

(Hints from google: yes, cause it's essential for network stability, fairness, and predictable performance). 
```

P5. Review the car-caravan analogy in Section 1.4. Assume a propagation speed of 100 km/hour.
a. Suppose the caravan travels 175 km, beginning in front of one tollbooth, passing through a second tollbooth, and finishing just after a third tollbooth. What is the end-to-end delay?
```sh
Processing delay: d(proc)
Queing delay: d(queue)
Tranmission delay: d(trans) = L/R
Propagation delay: d(prop) = d/s (assume s is 2.10^8 m/s)

d(nodal) = d(proc) + d(queue) + d(trans) + d(prop)
         =           2 minutes (120s) + (175 / (2.10^8))
```
b. Repeat (a), now assuming that there are eight cars in the caravan instead of ten.
```sh
Same formula, but instead of 120s, this time is 12 x 8 = 96s + (175 / 2.10^8)
```

P7. In this problem, we consider sending real-time voice from Host A to Host B over a packet-switched network (VoIP). Host A converts analog voice to a digital 64 kbps bit stream on the fly. Host A then groups the bits into 56-byte packets. There is one link between Hosts A and B; its transmission rate is 10 Mbps and its propagation delay is 10 msec. As soon as Host A gathers a packet, it sends it to Host B. As soon as Host B receives an entire packet, it converts the packet’s bits to an analog signal. How much time elapses from the time a bit is created (from the original analog signal at Host A) until the bit is decoded (as part of the analog signal at Host B)?
```sh
Transmission rate is 10 Mbps -> time delay is: packet size in bits / tranmission rate = 64 * 10 ^ 3 / 10 * 10^6 = 0.0064 ms
Propagation delay is 10 ms
Total time d(nodal) = d(trans) + d(prop) = 0.0064 + 10 = 10.0064
```

P8. Suppose users share a 10 Mbps link. Also suppose each user requires 200 kbps when transmitting, but each user transmits only 10 percent of the time. (See the discussion of packet switching versus circuit switching in Section 1.3.)
a. When circuit switching is used, how many users can be supported?
```sh
50 
```

b. For the remainder of this problem, suppose packet switching is used. Find the probability that a given user is transmitting.
```sh
Use binomial distribution, form the wikipedia, we can get:
F(n,k) = (n choose k) * (p^k) * (1 - p)^(n-k) 
```

c. Suppose there are 120 users. Find the probability that at any given time,
exactly n users are transmitting simultaneously. (Hint: Use the binomial
distribution.)
```sh
Each user transmit only 10 percent of the time -> so p = 0.1 and q = 0.9. 
F(120, 50) = (120 choose 50) * (0.1 ^ 50) * (0.9 ^ 70).
```

d. Find the probability that there are 51 or more users transmitting
simultaneously.
```sh
F(120, 51) = (120 choose 51) * (0.1 ^ 51) * (0.9 ^ 69).
```

P10. Consider the network illustrated in Figure 1.16. Assume the two hosts on the left of the figure start transmitting packets of 1500 bytes at the same time towards Router B. Suppose the link rates between the hosts and Router A is 4-Mbps. One link has a 6-ms propagation delay and the other has a 2-ms propagation delay. Will queuing delay occur at Router A?
```sh
R = 4 Mbps -> tranmission delay will be = (1500 bytes * 8) / (4 * 1024) = 12000 / 4 * 10^6 = 3ms 
First one: 6-ms propagation delay -> packet reaches route A at t = tramission delay + propagation delay = 3ms + 6ms = 9ms 
2nd one: 2-ms propagation delay -> packet reaches route A at t = 3m + 2ms = 5ms 

So, the answer is NO. 
```

P14. Consider the queuing delay in a router buffer. Let I denote traffic intensity; that is, I = La/R. Suppose that the queuing delay takes the form IL/R (1 - I) for I < 1.

a. Provide a formula for the total delay, that is, the queuing delay plus the transmission delay.
```sh
Total delay = IL/R (1-I) + L/R = L/(R*(1-I)) 
```

b. Plot the total delay as a function of L/R
![alt text](Figure_1.png)

P16. Consider a router buffer preceding an outbound link. In this problem, you will use Little’s formula, a famous formula from queuing theory. Let N denote the average number of packets in the buffer plus the packet being transmitted. Let a denote the rate of packets arriving at the link. Let d denote the average total delay (i.e., the queuing delay plus the transmission delay) experienced by a packet. Little’s formula is N = a * d. Suppose that on average, the buffer contains 100 packets, and the average packet queuing delay is 20 msec. The link’s transmission rate is 100 packets/sec. Using Little’s formula, what is the average packet arrival rate, assuming there is no packet loss?
```sh 
Average number of packets in the buffer + packet being transmitted: N
rate of packets arriving in the link: a  
average total delay (queuing + tranmission) by a packet: d 

Little's formual is N = a * d 
buffer: 100 packets 
average packet queuing delay: 20 ms = 0.02s 
Link's tranmission rate: 100 packets/s 

Arrival rate (a) = N / d = 100 / 0.02 
                         = 5000 packets/s 
```

P19. Metcalfe’s law states the value of a computer network is proportional to
the square of the number of connected users of the system. Let n denote the
number of users in a computer network. Assuming each user sends one message to each of the other users, how many messages will be sent? Does your
answer support Metcalfe’s law?
```sh
n is number of users in a computer network, if we send one message to each of them, that would be n * (n-1)  messages. 
```

P20. Consider the throughput example corresponding to Figure 1.20(b). Now suppose that there are M client-server pairs rather than 10. Denote Rs, Rc, and R for the rates of the server links, client links, and network link. Assume all other links have abundant capacity and that there is no other traffic in the network besides the traffic generated by the M client-server pairs. Derive a general expression for throughput in terms of Rs, Rc, R, and M.
```sh
T(pair) = min(Rs, Rc)

All M pairs if there were no bottleneck is M * T(pair)
Total throughput T in the network: T = min(M * min(RS, RC) R)

That possibly means 2 scenarios: 
(1) - If the total of M client-server pairs is less than the rate of network link, the throughput will be limited by the slower of client-server pairs. 
(2) - If the total of M client-server pairs is more than the rate of network link, the throughput will be limited by the network link. 
```

P21. Assume a client and a server can connect through either network (a) or (b) in
Figure 1.19. Assume that Ri = (Rc + Rs) / i, for i = 1, 2, ..., N. In what case
will network (a) have a higher throughput than network (b)?
```sh
The higher throughput should have smaller i, so the network (a) is the answer. 
```

P22. Consider Figure 1.19(b). Suppose that each link between the server and the client has a packet loss probability p, and the packet loss probabilities for these links are independent. What is the probability that a packet (sent by the server) is successfully received by the receiver? If a packet is lost in the path from the server to the client, then the server will re-transmit the packet. On average, how many times will the server re-transmit the packet in order for the client to successfully receive the packet?
```sh
Packet loss is independent, so the probability that a packet send by the server is successfully receved by the receiver is: P(success) = (1-p) ^ (number of packets). 

Using the geometric distribution, we have the probability of success P = (1- p)^n, then the expected number of tranmissions needed to successfully send a packet is 1 / (1- p)^n 

It will tell us on average, how many times it needed for the server re-transmist the packet in order for the client to successfully receive the packet. 
```

P23. Consider Figure 1.19(a). Assume that we know the bottleneck link along the path from the server to the client is the first link with rate Rs bits/sec. Suppose we send a pair of packets back to back from the server to the client, and there is no other traffic on this path. Assume each packet of size L bits, and both links have the same propagation delay dprop.

a. What is the packet inter-arrival time at the destination? That is, how much time elapses from when the last bit of the first packet arrives until the last bit of the second packet arrives?

```sh
The first packet time arrival time is: d(trans) + d(prop)
The 2nd packet time start immediately after the first packet: d(trans) + d(trans) + d(prop) = 2d(trans) + d(prop)
Delta(t1) = (t2 - t1) = d(trans) = R/S 
```

b. Now assume that the second link is the bottleneck link (i.e., Rc < Rs). Is
it possible that the second packet queues at the input queue of the second
link? Explain. Now suppose that the server sends the second packet T
seconds after sending the first packet. How large must T be to ensure no
queuing before the second link? Explain.
```sh
It's possible, when the 2nd packet arrives to the queue, the first one still being in the state of transmistting.  

For 2nd question, I have no idea :D 
```

P24. Consider a user who needs to transmit 1.5 gigabytes of data to a server. The user lives in a village where only dial-up access is available. As an alternative, a bus collects data from users in rural areas and transfer them to the Internet through a 1 Gbps link once it gets back to the city. The bus visits the village once a day and stops in front of the user’s house just long enough to receive the data. The bus has a 100 Mbps WiFi connection. Suppose the average speed of the bus is 60 km/h and that the distance between the village and the city is 150 km. What is the fastest way the user can transfer the data to the server?
```sh
Time to goes from his village to city t = d / s = 150 / 60 = 2.5 hours = 9000s. If we do not use Wifi but wait for the bus driver to go to the city and send through the Internet, it will take 9000s + 1.5s = 9001.5s. 

On the bus, WiFi will transfer 100 Mbps, so the needed time to transfer 1.5GB (1.5*1024^3*8) will be (1.5*1024^3*8) / (100 * 10^6) = 129s 

The fastest way the user can transfer the data to the server would be 15s (transferring on the bus through WiFi connection).
```

P27. Consider the scenario illustrated in Figure 1.19(a). Assume Rs is 20 Mbps, Rc is 10 Mbps, and the server is continuously sending traffic to the client. Also assume the router between the server and the client can buffer at most four messages. After how many messages sent by the server will packet loss starts occurring at the router?
```
Rs = 20 Mbps 
Rc = 10 Mbps 
Buffer: 4 message at most 

Rc is twice less than Rs. Assume it take 1s to transfer a packet from server to switch/router, and it takes 2s to transfer a packet from switch/router to end system. 

The first four packet will take 1s from s -> router. 
The first packet will take 2s from s -> router 
The 5th, 6th packet will take 1s from s -> router 
The 2nd packet will take 2s from s -> router 
The 7th packet will take 1s from s -> router 
The 8th packet will starting to be stucked.

And so on
=> So the answer will be the message 8th. 
```

Or should I use math for clarification? And this also the case for P28 
```sh
Denote the message is M (bits) -> the buffer size in bits will be 4 * M 

The time T to fill the buffer is: T = Buffer size / Rate of accumulation = 4*M / (20 - 10) * 10^6 

The number of messages sent by the server at rate of 20 Mbps: Rs*T / L / R = 20 * 10^6 * (4M / (10 * 10^6)) / M = 8 messages. 

That will be the same as above answer. 
```

P31. In modern packet-switched networks, including the Internet, the source host segments long, application-layer messages (for example, an image or a music file) into smaller packets and sends the packets into the network. The receiver then reassembles the packets back into the original message. We refer to this process as message segmentation. Figure 1.27 illustrates the end-to-end transport of a message with and without message segmentation. Consider a message that is 10^6 bits long that is to be sent from source to destination in Figure 1.27. Suppose each link in the figure is 5 Mbps. Ignore propagation, queuing, and processing delays.

a. Consider sending the message from source to destination without message segmentation. How long does it take to move the message from the source host to the first packet switch? Keeping in mind that each switch uses store-and-forward packet switching, what is the total time to move the message from source host to destination host?
```sh
T = L / R = 10^6 / (5 * 10^6) = 0.2s, we have 2 switches, so it needs to be triple (3 links between) -> 0.6s. 
```
b. Now suppose that the message is segmented into 100 packets, with each packet being 10,000 bits long. How long does it take to move the first packet from source host to the first switch? When the first packet is being sent from the first switch to the second switch, the second packet is being sent from the source host to the first switch. At what time will the second packet be fully received at the first switch?
```sh
Sigma L = L1 + L2 + ... + Ln with all Ln are the same. 
Time to move the first packet: T1 = L1 / R = 10000 / (5 * 10^6) = 0.002s 
The time which second packet be fulled received at the first witch is: 0.002 + T2 = 0.002 + 0.002 = 0.004s 
```

c. How long does it take to move the file from source host to destination host when message segmentation is used? Compare this result with your answer in part (a) and comment.
```sh
The total time can be calculated as:
(T1): The first packet transfer from source to destination (through 2 switches - 3 links) = 0.006s 
(T(total-packets-overlap)): The total of packets being overlap each others, except the first packet, we have 99 packets being overlapped. = (100 - 1) * 0.002 = 0.198s

Total T = T1 + T(total-packets-overlapp) = 0.006s + 0.198s = 0.204s 
```

d. In addition to reducing delay, what are reasons to use message
segmentation?
```sh
Faster, clear as day. 
```

e. Discuss the drawbacks of message segmentation
```sh
Packet loss -> Reassmbly issue
Latency issue 
Error handling complexity issue 
```

P33. Consider sending a large file of F bits from Host A to Host B. There are three links (and two switches) between A and B, and the links are uncongested (that is, no queuing delays). Host A segments the file into segments of S bits each and adds 80 bits of header to each segment, forming packets of L = 80 + S bits. Each link has a transmission rate of R bps. Find the value of S that minimizes the delay of moving the file from Host A to Host B. Disregard propagation delay.
```sh
The total number of packets: T(packets-total) = F / S 
The time for packet transfer from A to B: (80 + S) / R * 3
The time for over between 2 packets: T(overlapping) = (80 + S) / R
The total-time-overlapping for all the packets = 
the time for first packet + (T(packet-totals) - 1)*(T(overlapping)) 
= (80 + S / R * 3) + (F/S - 1) * (80 + S) / R 

Expand it, then we need to choose S as smallest as possible, could be 0. 
```

P34. Early versions of TCP combined functions for both forwarding and reliable delivery. How are these TCP variants located in the ISO/OSI protocol stack? Why were forwarding functions later separated from TCP? What were the consequences?
```sh
From ChatGPT, this approach had limitations:
Complexity: Combining forwarding and reliability made the TCP implementation complex.
Scalability: It was challenging to scale the system efficiently.
Resource Constraints: The same device had to manage both tasks, leading to resource constraints.

```