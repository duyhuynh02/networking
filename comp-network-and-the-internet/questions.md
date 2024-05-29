# HOMEWORK QUESTIONS

# SECTION 1.1
R1. What is the difference between a host and an end system? List several different types of end systems. Is a Web server an end system?

~~There is no difference. Host and end system is the same~~ 
-> Not all end systems are hosts, some end systems such as: switches and routers which faciliate data transfer but do not originate or terminate commucation sessions. 

```
Types of end system: server, computer, smartphone,... 
Yes. 
```


R2. Describe the protocol that might be used by two people having a telephonic conversation to initiate and end the conversation, i.e., the way that they talk.
```markdown
Someone says hello then someone also say hi for the reply, and it goes on. 
```

R3. Why are standards important for protocols?
```markdown
To follow the rule, we need to adapt and speak in the same way. 
```

## SECTION 1.2
R4. List four access technologies. Classify each one as home access, enterprise
access, or wide-area wireless access.
```markdown
Home access: DSL, Fiber Optic 
Enterprise access: Ethernet, Fiber Optic  
Wide-area wireless access: 3G, 4G, and 5G 
```

R5. Is HFC transmission rate dedicated or shared among users? Are collisions
possible in a downstream HFC channel? Why or why not?
```markdown
HFC is Hybrid Fiber-Coaxical, it shared among users 
No, it's not possible because 2 reasons: downstream communications in broadcast and controlled by the headend in the order. 
```

R6. What access network technologies would be most suitable for providing
internet access in rural areas?
```markdown
To save cost: DSL, Fiber Optic and 3G,4G and 5G. Nowadays we have satellite internet (such as SpaceX?)
```

R7. Dial-up modems and DSL both use the telephone line (a twisted-pair copper
cable) as their transmission medium. Why then is DSL much faster than dialup access?
```markdown
It dues to the fact that the DSL uses:
1. Wider frequency spectrum: allow for simultaneous voice and data tranmission.
2. Dedicated always-on connection
3. Employs advanced error correction and signal processing techniques
```

R8. What are some of the physical media that Ethernet can run over?
```markdown
Twisted-Paird Copper Cable (such as CAT5, CAT6, CAT6a, CAT7,...)
Fiber Optic Cable
Wireless 
Coaxical Cable 
```

R9. HFC, DSL, and FTTH are all used for residential access. For each of
these access technologies, provide a range of transmission rates and
comment on whether the transmission rate is shared or dedicated.

| Types | Range of transmission rates | Shared/Dedicated |
|-------|-----------------------------|------------------|
| HFC   | 25Mbps to 1GBps             | Shared           |
| DSL   | 256 Kbps to 100 Mbps        | Dedicated        |
| FTTH  | 100 Mbps to 10 Gbps         | Dedicated        |


R10. Describe the different wireless technologies you use during the day and their
characteristics. If you have a choice between multiple technologies, why do
you prefer one over another?
```markdown
It will depend on the broadrange and the speed, for instance, if you want to have a fast connection but in a low range, choose 5G. Instead, use lower (3G, 4G) to achieve the broader range connection. 
```

## SECTION 1.3
R11. Suppose there is exactly one packet switch between a sending host and a receiving host. The transmission rates between the sending host and the switch and between the switch and the receiving host are R1 and R2, respectively. Assuming that the switch uses store-and-forward packet switching, what is the total end-to-end delay to send a packet of length L? (Ignore queuing, propagation delay, and processing delay.)
```sh
The tranmission delay for each bit (packet) (first and second link) is L/R1 and L/R2 
The total of store-and-forward delay needs to wait for entire package to come then forward, therefore the store-and-forward delay = tramission delay1 + tranmission delay2 = 2L / R1 
Total end-to-delay includes both the tranmission delay and the store-and-forward delay which is: 2l/R1 + 2L/R2
```

R12. What advantage does a circuit-switched network have over a packet-switched network? What advantages does TDM have over FDM in a circuit-switched network?
```sh
It's dedicated resources, no sharing, it means that supports for just one purpose. 
FDM divided into frequency bands, meanwhile FSM didived into slots, that means each call allocated periodic slots, can transmit at maximum rate of (wider) frequency band. 
```

R13. Suppose users share a 2 Mbps link. Also suppose each user transmits continuously at 1 Mbps when transmitting, but each user transmits only 20 percent of the time. (See the discussion of statistical multiplexing in Section 1.3.)
a. When circuit switching is used, how many users can be supported?
```sh
2 
```
b. For the remainder of this problem, suppose packet switching is used. Why will there be essentially no queuing delay before the link if two or fewer users transmit at the same time? Why will there be a queuing delay if three users transmit at the same time?
```sh
Because the buffer can handle (max to 2 users), when the 3rd one arrives, the buffer is full, therefore it may become congested as it needs to accomodate 3 incoming packages. The result is the third user's packet must wait in the queue. 
```
c. Find the probability that a given user is transmitting.
```sh
20%
```
d. Suppose now there are three users. Find the probability that at any given time, all three users are transmitting simultaneously. Find the fraction of time during which the queue grows.
```sh
At any given time, all three users are transmitting simultatenously can be calculated by knowing that each user can only transmits 20 percent of the time (0.2). Therefore, for 3 of them running at the same time, it would be: 0.2^3 = 0.008 or 0.8 % (1) 

The fraction of time during which the queue grows (i.e., more than two users are tranmissiting simultaneously) = the prob that all 3 users are transmitting simutenously (1) + the prob of exactly two users transmitting (2)

The prob of two users transmitting and one user not transmitting is: P(transmitting)^2 * P(not transmitting) = 0.2 * 0.2 * 0.8 = 0.032 (3)

How many ways to choose exactly two out of three? It's 3. (4)

From (3) and (4), we will have the prob of exactly 2 users transmitting: 0.032 * 3 = 0.096, replaced to to (2)

The final answer is: 0.008 + 0.096 = 0.104 or 10.4% 

```

R14. Why will two ISPs at the same level of the hierarchy often peer with each other? How does an IXP earn money?
```sh
To save the money, improve performance, and network reachability. IXP comes into place to adapt (or make it as an API as a software term) for all the networks who want to join as a cross-reference. 
```

R15. Why is a content provider considered a different Internet entity today? How does a content provider connect to other ISPs? Why?
```sh
Content provider (like Facebook/Google/AMZ) also want to deliver fast speed (maybe instantly) so it also want to become Tier 1 ISP. 
```

## SECTION 1.4
R16. Consider sending a packet from a source host to a destination host over a fixed route. List the delay components in the end-to-end delay. Which of these delays are constant and which are variable?
```sh
Processing delay: the time needed for a intermediate router/node to process a package  | variable 
Tranmission delay: the time needed for a packet being transferred from host to tranmission medium | constant 
Queueing delay: packets in buffers (waiting in the buffer while being proceeded) | variable 
Propagation delay: time taken for the last bit of a packet to travel from host to the destination | constant 
```

R17. Visit the Transmission Versus Propagation Delay interactive animation at the Companion Website. Among the rates, propagation delay, and packet sizes available, find a combination for which the sender finishes transmitting before the first bit of the packet reaches the receiver. Find another combination for which the first bit of the packet reaches the receiver before the sender finishes transmitting.
```sh
(1) A combination for which the sender finishes transmitting before the first bit of the packet reaches the receiver => tranmission delay < propagation delay 


(2) Another combination for which the first bit of the packet reaches the receiver before the sender finishes transmitting: tranmission delay > propagation delay 

You do the math. 
```

R18. A user can directly connect to a server through either long-range wireless or a twisted-pair cable for transmitting a 1500-bytes file. The transmission rates of the wireless and wired media are 2 and 100 Mbps, respectively. Assume that the propagation speed in air is 3 * 108 m/s, while the speed in the twisted R16. Consider sending a packet from a source host to a destination host over a fixed route. List the delay components in the end-to-end delay. Which of these delays are constant and which are variable?
```sh
1500-byte file 
tranmission rates:
 wireless: 2 Mbps 
 wired media: 100 Mbps 
propagation speed: 3 * 10^8 m/s

The delay component in the end-to-end delay: 
Same as R16 
```

R19. Suppose Host A wants to send a large file to Host B. The path from Host A to Host B has three links, of rates R1 = 500 kbps, R2 = 2 Mbps, and R3 = 1 Mbps.
a. Assuming no other traffic in the network, what is the throughput for the file transfer?
```sh
Should be the smallest one, it means R1: 500 Kbps. 
```
b. Suppose the file is 4 million bytes. Dividing the file size by the throughput, roughly how long will it \ take to transfer the file to Host B?
```sh
Convert 1 kbps to byte = 1000 bits per second (bps) = 125 bytes per second 
So 500 kbps = 500 * 125 = 62500 (bytes per second)

The result is: 4,000,000 / 62,500 = 64s. 
```
c. Repeat (a) and (b), but now with R2 reduced to 100 kbps. 
```sh
Do the same. 
```

R20. Suppose end system A wants to send a large file to end system B. At a very high level, describe how end system A creates packets from the file. When one of these packets arrives to a router, what information in the packet does the router use to determine the link onto which the packet is forwarded? Why is packet switching in the Internet analogous to driving from one city to another and asking directions along the way?
```sh
It will need a protocol header for, for example, a TCP/IP protocol, size of each segment (MTU - Maximum Transmission Unit) of the network, then a payload. 
Assume we have 4,000,000 bytes file, it will take:
MTU: 1500 bytes 
IP header: 20 bytes
TCP header: 20 bytes
Payload: 1460 bytes (1500 - 20 - 20)

Then the number of packets will be: total file size (4000000) / payload size (1500) = 2740 segments. 
```

R21. Visit the Queuing and Loss interactive animation at the Companion Website. What is the maximum emission rate and the minimum transmission rate? With those rates, what is the traffic intensity? Run the interactive animation with these rates and determine how long it takes for packet loss to occur. Then repeat the experiment a second time and determine again how long it takes for packet loss to occur. Are the values different? Why or why not?
```sh
Maximum emission rate: 500 packets/s
Mininum emission rate: 350 packets/s 

Traffic intensity: arrival rate of bits / service rate of bits (L * a / R)
a: average packet arrival rate 
L: packet length (bits)
R: link bandwidth (bit tranmission rate) 

Assume package length is 1000 bits => (500 + 350) / 2 * 1000 / 500 (assume tranmission rate is 500) = 425. 

```