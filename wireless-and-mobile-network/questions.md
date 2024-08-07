# HOMEWORK QUESTIONS
Questions in the textbook. Decided to answer most of the questions here. 

## SECTION 7.1
R1. What does it mean for a wireless network to be operating in “infrastructure mode”? If the network is not in infrastructure mode, what mode of operation is it in, and what is the difference between that mode of operation and infrastructure mode?
```sh
That means all traditional networks (e.g., address assigment and routing) are provided by the network to which a host is connected via the base station. 

Ad hoc networks, basically there is no such infrastructure with which to connect. Therefore, the hosts themselves must provide for services such as routing, address assignment, DNS-like name translation. 
```

R2. Both MANET and VANET are multi-hop infrastructure-less wireless networks. What is the difference between them?
```sh
If the mobile nodes are vehicles, the network is a vehicular ad hoc network. (VANETs)
If the node is mobile, with connectivity changing among nodes -> mobile ad hoc network (MANETs)
```

## SECTION 7.2
R3. What are the differences between the following types of wireless channel impairments: path loss, multipath propagation, interference from other sources?

| Path loss | Multipath propagation | Interference from other sources | 
|-----------|-----------------------|---------------------------------|
| decrease signal strength when pass through matter (e.g., wall) | electromagnetic wave reflect off objects and the ground, taking paths of different lengths | Radio source transmit in the same frequency band will interfere with each other 


R4. As a mobile node gets farther and farther away from a base station, what are two actions that a base station could take to ensure that the loss probability of a transmitted frame does not increase?
```sh
- Increase transmission power 
- Adjust modulation and coding scheme e.g., from 64-QAM to QPSK to increase the level of error correction coding. This reduces the data race but improves the reliability of the transmitted frames, helping to maintain low loss probability. 
```

## SECTION 7.3
R5. Describe the role of the beacon frames in 802.11.
```sh
The wireless device (e.g., your device) knows that APs are sending beacon frames, scan the 11 channels, then seeking beacon frames from any APs that may be out there, learn about it then select one of the APs for association. 
```
R6. An access point periodically sends beacon frames. What are the contents of the beacon frames?
```sh
Each beacon frames contain AP's SSID and MAC address.
```
R7. Why are acknowledgments used in 802.11 but not in wired Ethernet?
```sh
Because of the relatively high bit error rates of wireless channel.
```
R8. What is the difference between passive scanning and active scanning?
| Passive scanning | Active scanning | 
|------------------|-----------------|
|Process of scanning channels and listening for beacon frames| Broadcasting a probe frame that will be received by all APs within the wireless device's range -> then AP response to the probe request frame with a probe response frame.|

R9. What are the two main purposes of a CTS frame?
```sh
- Give the sender explicit permission to send 
- Instructs the other stations not to send for the reversed duration 
```
R10. Suppose the IEEE 802.11 RTS and CTS frames were as long as the standard DATA and ACK frames. Would there be any advantage to using the CTS and RTS frames? Why or why not?
```sh
No, the purpose of using CTS and RTS is because of their short length, a collision involving an RTS or CTS frame will last only the duration of the short RTS or CTS frame. Once the RTS
and CTS frames are correctly transmitted, the following DATA and ACK frames
should be transmitted without collisions
```
R11. Section 7.3.4 discusses 802.11 mobility, in which a wireless station moves from one BSS to another within the same subnet. When the APs are interconnected with a switch, an AP may need to send a frame with a spoofed MAC address to get the switch to forward the frame properly. Why?
```sh
To get the switch update fast to the forwarding table, sounds like a hack (according to Google, it may be the quickest way). If not, the switch might continue sending frames to the old AP until it eventually times out the old MAC address entry, leading to frame loss or delays 
```

R12. What is the difference between Bluetooth and Zigbee in terms of data rate?
```sh
Bluetooth: up to 3 Mbps for 4.0 and 50 Mbps for 5.0 
Zigbee: around 250 kbps 
```

R13. What is the role of the base station in 4G/5G cellular architecture? With which other 4G/5G network elements (mobile device, MME, HSS, Serving Gateway Router, PDN Gateway Router) does it directly communicate with in the control plane? In the data plane?
```sh
Control Plane:
4G: eNodeB <--> UE, MME, HSS (indirectly)
5G: gNodeB <--> UE, AMF, UDM (indirctly)

Data Plane:
4G: eNodeB <-> SGW, PGW 
5G: gNodeB <-> UDF, SMF
```
R14. What is an International Mobile Subscriber Identity (IMSI)?
```sh
IMSI is an unique number assigned to every user of a cellular network for authentication and seamless communication and roaming. 
```
R15. What is the role of the Home Subscriber Service (HSS) in 4G/5G cellular architecture? With which other 4G/5G network elements (mobile device, base station, MME, Serving Gateway Router, PDN Gateway Router) does it directly communicate with in the control plane? In the data plane?
```sh
Located in a mobile device's home network, provide authentication, access privileges in home and visited networks 

2nd question: Check R13 
```
R16. What is the role of the Mobility Management Entity (MME) in 4G/5G cellular architecture? With which other 4G/5G network elements (mobile device, base station, HSS, Serving Gateway Router, PDN Gateway Router) does it directly communicate with in the control plane? In the data plane?
```sh
MME: Coordinator for mobile device services: authentication, mobility managemention

2nd question: Check R13 
```

R17. Describe the purpose of two tunnels in the data plane of the 4G/5G cellular architecture. When a mobile device is attached to its own home network, at which 4G/5G network element (mobile device, base station, HSS, MME, Serving Gateway Router, PDN Gateway Router) does each end of each of the two tunnels terminate?
```sh
n/a 
```
R18. What are the three sublayers in the link layer in the LTE protocol stack? Briefly describe their functions.
```sh
Packet Data Convergence: performs IP header/compression to decrease bit number of bits sent over the wireless link, encryption/decryption of the IP datagram
Radio Link Control: fragmenting and reassembly 
Medium Access Control (MAC): transmission scheduling (or requesting and use of the radio transmisting slot)
```
R19. Does the LTE wireless access network use FDMA, TDMA, or both? Explain your answer.
```sh
Yes, it uses a combination of FDMA and TDMA known as orthogonal frequncy division multiplexing (OFDM)
```
R20. Describe the two possible sleep modes of a 4G/5G mobile device. In each of these sleep modes, will the mobile device remain associated with the same base station between the time it goes to sleep and the time it wakes up and first sends/receives a new datagram?
```sh
Light sleep mode: periodically wakes up (every few hundred miliseconds) to check for any incoming data or control messages -> remains associated with the same base station 

Deep sleep mode: In deep sleep mode, the device significantly reduces its power consumption by shutting down more components. It wakes up less frequently compared to light sleep mode. -> may change cells 
```
R21. What is meant by a “visited network” and a “home network” in 4G/5G cellular architecture?
| Visited network | Home network |
|-----------------|--------------|
| is the subscriber's primary network, where their subscription and user profiles are stored | any network other than the subscriber's home network that they connect to while roaming | 
|responsible for authetication, managing the subscription details, providing services like billing and customer support | provides local connectivity and services to the subscriber while they are away from their home network | 

R22. List three important differences between 4G and 5G cellular networks.
| Keys difference | 4G network | 5G network | 
|-----------------|------------|------------|
| Speed | up to 1 Gbps - real word around 10-50 Mbps | up to 20 Gbps, real world 50 Mbps - 3 Gbps | 
| Latency | around 50 milliseconds | low as 1 miliseconds |
| Capacity and Efficiency | support fewer devices per unit area and has limit in handling high data traffic | support a massive number of devices per unit area, imporving network capacity and efficiency | 

## SECTION 7.5
R23. What does it mean that a mobile device is said to be “roaming?”
```sh
Roaming means you can jump from one network (home network) to other network (visited network) without disconnection. That means it allows the device to automatically make and receive calls, send and receive data, and access other services using the visted network -> providng seamless and access to services. 
```
R24. What is meant by “hand over” of a network device?
```sh
Check R23, basically it refers to the process of transferring an ongoing call/data session from 1 base state to another without interruption. 
```
R25. What is the difference between direct and indirect routing of datagrams to/ from a roaming mobile host?
| Direct routing | Indirect routing |
|----------------|------------------|
| datagrams are sent directly to the current location of the mobile without passing through intermediate nodes | datagrams are first sent to the home network and then forwarded to the current location of the mobile host 
| Move efficient with lower latency but requires the home agent to track the mobile host's location | easy to implement |


R26. What does “triangle routing” mean?
```sh
Data packets travel in a triangular path: from the correspondent node -> home agent -> mobile host via the foreign agent. 
```

## SECTION 7.6
R27. Describe the similarity and differences in tunnel configuration when a mobile device is resident in its home network, versus when it is roaming in a visited network. 
| Home network | Visited network |
|--------------|-----------------|
| Use its own IP address | Use a care-of address assigned by the visited network | 
| Routed directly to the mobile device using standard IP routing | Data packets are first sent to the network then Home Agent intecepts these packets and tunnels them to the care-of address in the visited network | 

R28. When a mobile device is handed over from one base station to another in a 4G/5G network, which network element makes the decision to initiate that handover? Which network element chooses the target base station to which the mobile device will be handed over?
| Type | 4G network | 5G Network |
|------|------------|------------|
| Decision to initiate handover | eNodeB| gNodeB |
| Choosing the target base station | eNodeB and MME (Mobility Management Entity) | gNodeB and AMF (Access and Mobility Management Function) 

R29. Describe how and when the forwarding path of datagrams entering the visited network and destined to the mobile device changes before, during, and after hand over.
```sh
Before: Datagrams are routed to home network (HA) to the devices. 

During: Datagrams are tunnel from HA to the FA in the visited network and then forwarded to the devices  

After: Datagrams are directly routed from the HA to the FA in the visited network, with the FA forwarding to the devices. 
```

## SECTION 7.7
R31. What are three approaches that can be used to avoid having a single wireless
link degrade the performance of an end-to-end transport-layer TCP connection?
```sh
Later
```