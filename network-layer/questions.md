# HOMEWORK QUESTIONS
Questions in the textbook. Decided to answer most of the questions here. 

## Section 4.1 
R1. Let’s review some of the terminology used in this textbook. Recall that the name of a transport-layer packet is segment and that the name of a link-layer packet is frame. What is the name of a network-layer packet? Recall that both routers and link-layer switches are called packet switches. What is the fundamental difference between a router and link-layer switch?
```sh
Name of the network-layer packet:  datagram 
The difference between both is while router can handle on layer 3 with IP address, link-layer switch can handle inter-communication on both layer 2 and 3 based on the IP address and MAC address. 
```
R2. We noted that network layer functionality can be broadly divided into data plane functionality and control plane functionality. What are the main functions of the data plane? Of the control plane?
```sh
Data plane: routing 
Control: forwarding 
```
R3. We made a distinction between the forwarding function and the routing function performed in the network layer. What are the key differences between routing and forwarding?
```sh
Routing: plan everything before you go
Forwarding: actually go 
```
R4. What is the role of the forwarding table within a router?
```sh
To know which device a router need to send the datagram for in a network (among routers and routers)
```
R5. We said that a network layer’s service model “defines the characteristics of end-to-end transport of packets between sending and receiving hosts.” What is the service model of the Internet’s network layer? What guarantees are made by the Internet’s service model regarding the host-to-host delivery of datagrams?
```sh
There is no guarantee, in bandwidth usage, in loss, or in everything. 
```

## Section 4.2
R6. In Section 4.2, we saw that a router typically consists of input ports, output ports, a switching fabric and a routing processor. Which of these are implemented in hardware and which are implemented in software? Why? Returning to the notion of the network layer’s data plane and control plane, which are implemented in hardware and which are implemented in software? Why?
```sh
These are implemented 
in software: input ports, output ports, switching fabric 
in hardward: routing processor 
```
R7. How can the input ports of a high-speed router facilitate fast forwarding decisions?
```sh
Digh-speed router means higher throughput (input & output) and maybe use more advanced algorithm to handle decisions, no? 
```
R8. What is meant by destination-based forwarding? How does this differ from generalized forwarding (assuming you’ve read Section 4.4, which of the two approaches are adopted by Software-Defined Networking)?
```sh
Destination-based forwarding means you already have an IP address (or destination) in mind. 
```
R9. Suppose that an arriving packet matches two or more entries in a router’s forwarding table. With traditional destination-based forwarding, what rule does a router apply to determine which of these rules should be applied to determine the output port to which the arriving packet should be switched?
```sh
If there are two or more, we choose the first one. In case which has more same bits, we choose the bigger. 
```
R10. Switching in a router forwards data from an input port to an output port. What is the advantage of switching via an interconnection network over switching via memory and switching via bus?
```sh
It's more simpler and cheaper, and some cases, we do not need that much complexity. 
```
R11. What is the role of a packet scheduler at the output port of a router?
```sh
Forwarding? 
```
R12. a. What is a drop-tail policy?
```sh
A simple algorithm using in the queue, if there is no space for the new packet, it will drop the new arriving packet. 
```
b. What are AQM algorithms?
```sh
According to google, AQM stands for Acceptant Quality Limit. I have no idea :D 
```
c. Name one of the most widely studied and implemented AQM algorithms and explain how it works.
```sh
Random Early Detection 
```
R13. What is HOL blocking? Does it occur in input ports or output ports?
```sh
A phenomenon-limiting occurs when a line packet being held up by the first packet in the queue. So it should happen in input ports. 
```
R14. In Section 4.2, we studied FIFO, Priority, Round Robin (RR), and Weighted Fair Queuing (WFQ) packet scheduling disciplines? Which of these queuing disciplines ensure that all packets depart in the order in which they arrived?
```sh
FIFO - first in first out 
```
R15. Give an example showing why a network operator might want one class of packets to be given priority over another class of packets.
```sh
VoiP > Email 
```
R16. What is an essential different between RR and WFQ packet scheduling? Is there a case (Hint: Consider the WFQ weights) where RR and WFQ will behave exactly the same?
```sh
RR focuses more on the fairness, meanwhile WFQ focuses on the quality (or weight)
When weight is the same for all the packets. 
```

## Section 4.3
R17. Suppose Host A sends Host B a TCP segment encapsulated in an IP datagram. When Host B receives the datagram, how does the network layer in Host B know it should pass the segment (that is, the payload of the datagram) to TCP rather than to UDP or to some other upper-layer protocol?
```sh

```
R18. What field in the IP header can be used to ensure that a packet is forwarded through no more than N routers?
```sh

```
R19. Recall that we saw the Internet checksum being used in both transport-layer segment (in UDP and TCP headers, Figures 3.7 and 3.29 respectively) and in network-layer datagrams (IP header, Figure 4.17). Now consider a transport layer segment encapsulated in an IP datagram. Are the checksums in the segment header and datagram header computed over any common bytes in the IP
datagram? Explain your answer.
```sh

```

R20. When a large datagram is fragmented into multiple smaller datagrams, where are these smaller datagrams reassembled into a single larger datagram?
```sh

```
R21. How many IP addresses does a router have?
```sh

```
R22. What is the 32-bit binary equivalent of the IP address 202.3.14.25?
```sh

```
R23. Visit a host that uses DHCP to obtain its IP address, network mask, default router, and IP address of its local DNS server. List these values.
```sh

```
R24. Suppose there are four routers between a source host and a destination host. Ignoring fragmentation, an IP datagram sent from the source host to the destination host will travel over how many interfaces? How many forwarding tables will be indexed to move the datagram from the source to the destination?
```sh

```
R25. Suppose an application generates chunks of 40 bytes of data every 20 msec, and each chunk gets encapsulated in a TCP segment and then an IP datagram. What percentage of each datagram will be overhead, and what percentage will be application data?
```sh

```
R26. Suppose you purchase a wireless router and connect it to your cable modem.
Also suppose that your ISP dynamically assigns your connected device (that
is, your wireless router) one IP address. Also suppose that you have five PCs
at home that use 802.11 to wirelessly connect to your wireless router. How
are IP addresses assigned to the five PCs? Does the wireless router use NAT?
Why or why not?
```sh

```
R27. What is meant by the term “route aggregation”? Why is it useful for a router
to perform route aggregation?
```sh

```
R28. What is meant by a “plug-and-play” or “zeroconf” protocol?
```sh

```
R29. What is a private network address? Should a datagram with a private network
address ever be present in the larger public Internet? Explain.
```sh

```
R30. Compare and contrast the IPv4 and the IPv6 header fields. Do they have any
fields in common?
```sh

```
R31. It has been said that when IPv6 tunnels through IPv4 routers, IPv6 treats the
IPv4 tunnels as link-layer protocols. Do you agree with this statement? Why
or why not?
```sh

```

## Section 4.4
R32. How does generalized forwarding differ from destination-based forwarding?
```sh

```
R33. What is the difference between a forwarding table that we encountered in
destination-based forwarding in Section 4.1 and OpenFlow’s flow table that
we encountered in Section 4.4?
```sh

```
R34. What is meant by the “match plus action” operation of a router or switch? In
the case of destination-based forwarding packet switch, what is matched and
what is the action taken? In the case of an SDN, name three fields that can be
matched, and three actions that can be taken.
```sh

```
R35. Name three header fields in an IP datagram that can be “matched” in OpenFlow 1.0 generalized forwarding. What are three IP datagram header fields
that cannot be “matched” in OpenFlow?
```sh

```