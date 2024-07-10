# Labs - Wireshark 
If you're unable to run Wireshark on a live network connection or are answering question via an LMS (Learning Management System), you can download a packet trace file that was captured while following the steps above by Wireshark captured packet file tcp-wireshark-trace1-1 in http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces-8.1.zip 

## 2. A first look at the captured trace 
1. What is the IP address and TCP port number used by the client computer (source) that is transferring the alice.txt file to gaia.cs.umass.edu? To answer this question, it’s probably easiest to select an HTTP message and explore the details of the TCP packet used to carry this HTTP message, using the “details of the selected packet header window” (refer to Figure 2 in the “Getting Started with Wireshark” Lab if you’re uncertain about the Wireshark windows).
```sh
IP address: 192.168.31.26
TCP port number: 50260
```
2. What is the IP address of gaia.cs.umass.edu? On what port number is it sending and receiving TCP segments for this connection?
```sh
Dest port: 128.119.245.12 
TCP port number: 80 
```

## 3. TCP Basics 
3. What is the sequence number of the TCP SYN segment that is used to initiate the TCP connection between the client computer and gaia.cs.umass.edu? (Note: this is the “raw” sequence number carried in the TCP segment itself; it is NOT the packet # in the “No.” column in the Wireshark window. Remember there is no such thing as a “packet number” in TCP or UDP; as you know, there are sequence numbers in TCP and that’s what we’re after here. Also note that this is not the relative sequence number with respect to the starting sequence number of this TCP session.). What is it in this TCP segment that identifies the segment as a SYN segment? Will the TCP receiver in this session be able to use Selective Acknowledgments (allowing TCP to function a bit more like a “selective repeat” receiver, see section 3.4.5 in the text)?
```sh
Sequence Number: 0    (relative sequence number)
Sequence Number (raw): 2120616048
[Next Sequence Number: 1    (relative sequence number)]
Acknowledgment Number: 0
Acknowledgment number (raw): 0
```

4. What is the sequence number of the SYNACK segment sent by gaia.cs.umass.edu to the client computer in reply to the SYN? What is it in the segment that identifies the segment as a SYNACK segment? What is the value of the Acknowledgement field in the SYNACK segment? How did gaia.cs.umass.edu determine that value?
```sh
Sequence Number: 0    (relative sequence number)
Sequence Number (raw): 940230358
[Next Sequence Number: 1    (relative sequence number)]

Identified: Flags: 0x012 (SYN, ACK)

Acknoledgement field in the SYNACK segment: 
Acknowledgment Number: 1    (relative ack number)
Acknowledgment number (raw): 2120616049

```
5. What is the sequence number of the TCP segment containing the header of the HTTP POST command? Note that in order to find the POST message header, you’ll need to dig into the packet content field at the bottom of the Wireshark window, looking for a segment with the ASCII text “POST” within its DATA field4,5. How many bytes of data are contained in the payload (data) field of this TCP segment? Did all of the data in the transferred file alice.txt fit into this single segment?
```sh
Sequence Number: 1    (relative sequence number)
Sequence Number (raw): 450988042
Bytes of data in the payload: [Content length: 152319]
All of the data transfer? -> No. 
```
6. Consider the TCP segment containing the HTTP “POST” as the first segment in the data transfer part of the TCP connection.

At what time was the first segment (the one containing the HTTP POST) in the data-transfer part of the TCP connection sent?
```sh
212 8.22805
```
At what time was the ACK for this first data-containing segment received?
```sh
226	8.55485
```

What is the RTT for this first data-containing segment?
```sh
0.3268 
```
What is the RTT value the second data-carrying TCP segment and its ACK?
```sh
224	8.43945 (you do the math.)
```
What is the EstimatedRTT value (see Section 3.5.3, in the text) after the ACK for the second data-carrying segment is received? Assume that in making this calculation after the received of the ACK for the second segment, that the initial value of EstimatedRTT is equal to the measured RTT for the first segment, and then is computed using the EstimatedRTT equation on page 242, and a value of a = 0.125.
```sh

```

7. What is the length (header plus payload) of each of the first four data-carrying TCP segments?
```sh
1448 bytes (including 20 bytes header)
```
8. What is the minimum amount of available buffer space advertised to the client by gaia.cs.umass.edu among these first four data-carrying TCP segments7? Does the lack of receiver buffer space ever throttle the sender for these first four data-carrying segments?
```sh
Window: 2058
I guess... no? 
```
9. Are there any retransmitted segments in the trace file? What did you check for (in the trace) in order to answer this question?
```sh
Yes, it showed in back color and also have a "retranmission" on it. 
For example, 
397	18.181895	192.168.31.26	52.168.112.66	TCP	66	[TCP Dup ACK 394#1] 49796 → 443 [ACK] Seq=5050 Ack=428 Win=1029 Len=0 SLE=330 SRE=428
```
10. How much data does the receiver typically acknowledge in an ACK among the first ten data-carrying segments sent from the client to gaia.cs.umass.edu? Can you identify cases where the receiver is ACKing every other received segment (see Table 3.2 in the text) among these first ten data-carrying segments?
```sh
14480 
```
11. What is the throughput (bytes transferred per unit time) for the TCP connection? Explain how you calculated this value.
```sh
Throughput = Total data in bytes / RTT 
```

## 4. TCP congestion control in action 
12. Use the Time-Sequence-Graph(Stevens) plotting tool to view the sequence number versus time plot of segments being sent from the client to the gaia.cs.umass.edu server. Consider the “fleets” of packets sent around t = 0.025, t = 0.053, t = 0.082 and t = 0.1. Comment on whether this looks as if TCP is in its slow start phase, congestion avoidance phase or some other phase. Figure 6 shows a slightly different view of this data.
```sh
Yeah since it does not add up to the sequence number and reach the slow start threshold (ssthresh), it should be congestion avoidance phase. 
```
13. These “fleets” of segments appear to have some periodicity. What can you say about the period?
```sh
I have no idea, stable? 
```
14. Answer each of two questions above for the trace that you have gathered when you transferred a file from your computer to gaia.cs.umass.edu
```sh

```