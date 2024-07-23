# HOMEWORK QUESTIONS
Questions in the textbook. Decided to answer most of the questions here. 

## Section 6.1–6.2
R1. What is framing in link layer?
```sh
Framing includes a packet (with header and IP datagram)
```
R2. If all the links in the Internet were to provide reliable delivery service, would the TCP reliable delivery service be redundant? Why or why not?
```sh
No it's not. Even though we can provide reliable deliversy service on the link layer, it would consume too much resources. 
```
R3. Name three error-detection strategies employed by link layer.
```sh
Parity check: sender adds a new extra bit to the datafram, the parity bit ensure that the total of 1s in the frame is either all odd or even, then receiver check the parity bit to detect single-bit errors

Checksum: data is divided into fixed-size segments (frames) -> sender compute the sum of all the segments by using 1s's complement arithmetic -> sender complements the sum to obtain the checksum -> send it to recever with data frames and checksum -> receiver recevies it and compute it again and compare the checksum. 

CRC: sender treats data as a binary polynomial -> sender divides a binary polymonial by the fixed divisor using modulo-2 division to get the remainder -> send data plus remainder to receiver -> receiver receives then use same process then compare. 
```

## Section 6.3 
R4. Suppose two nodes start to transmit at the same time a packet of length L over a broadcast channel of rate R. Denote the propagation delay between the two nodes as d prop. Will there be a collision if d(prop) < L/R? Why or why not?
```sh
Yes, the time for tranmission is L/R. But d(prop) < L/R means the signal from node A will reach node B (or vice versa) before it fully finished transmitting its packet. 
```
R5. In Section 6.3, we listed four desirable characteristics of a broadcast channel. Which of these characteristics does slotted ALOHA have? Which of these characteristics does token passing have?
```sh
High throughput, fairness, low latency and scalability 
```
| Type | ALOHA | Token Passing | 
|------|-------|---------------|
| High throughput | Moderate (slotted ALOHA is better ~ 1/e ~ 36.8%) | High (collion-free)
| Fairness | Moderate (random access, potential periods of unfairness) | Moderate (equal opport. for all nodes)
| Low latency | Variable | Low in small networks 
| Scability | Poor | Good 

R6. In CSMA/CD, after the fifth collision, what is the probability that a node chooses K = 4? The result K = 4 corresponds to a delay of how many seconds on a 10 Mbps Ethernet?
```sh
No idea. 
```
R7. While TDM and FDM assign time slots and frequencies, CDMA assigns a different code to each node. Explain the basic principle in which CDMA works.
```sh
Each users are assigned a unique code, then spread all around the network. CDMA shares the frequency band without interference.
```
R8. Why does collision occur in CSMA, if all nodes perform carrier sensing before transmission?
```sh
Not used in full-duplex operation, so if both nodes are in middle of tranmission, it will cause collision. 
```