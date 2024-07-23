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

## Section 6.4
R9. How big is the MAC address space? The IPv4 address space? The IPv6 address space?
```sh
MAC address: 2^48 = 281,474,976,710,656
IPv4: 32-bit address length -> 2^32 = 4,294,967,296
IPv6: 128-bit address length -> 2^128 = 340,282,366,920,938,463,463,374,607,431,768,211,456 (that means you can count every sand on the planet)
```
R10. Suppose nodes A, B, and C each attach to the same broadcast LAN (through their adapters). If A sends thousands of IP datagrams to B with each encapsulating frame addressed to the MAC address of B, will C’s adapter process these frames? 
```sh
Yes
```
If so, will C’s adapter pass the IP datagrams in these frames to the network layer C? 
```sh
No
```
How would your answers change if A sends frames with the MAC broadcast address?
```sh
For MAC broadcast address, that means it sends to all the node in LAN (ok the MAC address is FF:FF:FF:FF:FF) then the answer will be yes for both. 
```
R11. IEEE manages the MAC address space, allocating chunks of it to companies manufacturing network adapters. The first half of the bits of the addresses in these chunks are fixed, ensuring that the address space is unique. How long will a chunk last for a company manufacturing 1,000,000 network adapters per year?
```sh
2^24 / 1,000,000 = 16.78 ~ 17 years. 
```
R12. For the network in Figure 6.19, the router has two ARP modules, each with its own ARP table. Is it possible that the same MAC address appears in both tables?
```sh
Yes, if node A request a MAC address of node B through switch SW, then both node A and switch SW will appears in both tables. 
```
R13. What is a hub used for?
```sh
Hub has the same functionality as routers/switches, but hubs do not make intelligent forwarding so it's being replaced. 
```
R14. Consider Figure 6.15. How many subnetworks are there, in the addressing sense of Section 4.3?
```sh
3
```
R15. Each host and router has an ARP table in its memory. What are the contents of this table?
```sh
IP address (layer 3 - network layer) and MAC address (layer 2 - data link layer)
```
R16. The Ethernet frame begins with an 8-byte preamble field. The purpose of the first 7 bytes is to “wake up” the receiving adapters and to synchronize their clocks to that of the sender’s clock. What are the contents of the 8 bytes? What is the purpose of the last byte?
```sh
The contents of the first 7 bytes is 10101010 
The last byte is set to 10101011, indicates that the upcoming bits represent the destination address. (SFD - or Start of Frame Delimiter), servers as a final sync signal, warning stations that this is the last change to sync before the actual frame begin.
```