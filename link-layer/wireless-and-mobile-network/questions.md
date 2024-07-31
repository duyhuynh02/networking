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