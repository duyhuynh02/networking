# Labs - Wireshark 
If you're unable to run Wireshark on a live network connection or are answering question via an LMS (Learning Management System), you can download a packet trace file that was captured while following the steps above by Wireshark captured packet file tcp-wireshark-trace1-1 in http://gaia.cs.umass.edu/wireshark-labs/wireshark-traces-8.1.zip 

## The assignment
1. Select the first UDP segment in your trace. What is the packet number of this segment in the trace file? What type of application-layer payload or protocol message is being carried in this UDP segment? Look at the details of this packet in Wireshark. How many fields there are in the UDP header? (You shouldn’t look in the textbook! Answer these questions directly from what you observe in the packet trace.) What are the names of these fields?
```sh
Packet number: 5 
Type of application-layer payload/protocol message being carried in this UDP segment: SSDP
Number of fields: 4 (including srt port, dest port, length, checksum)
```
2. By consulting the displayed information in Wireshark’s packet content field for this packet (or by consulting the textbook), what is the length (in bytes) of each of the UDP header fields?
```sh
20 bytes 
```
3. The value in the Length field is the length of what? (You can consult the text for this answer). Verify your claim with your captured UDP packet.
```sh
Indicate the data (payload) and the header byte 
```
4. What is the maximum number of bytes that can be included in a UDP payload? (Hint: the answer to this question can be determined by your answer to 2. above)
```sh
512 bytes 
```
5. What is the largest possible source port number? (Hint: see the hint in 4.)
```sh
UDP uses an unsigned 16-bit integer so it should be from range 0 to 65535. The answer is 65535
```
6. What is the protocol number for UDP? Give your answer in decimal notation. To answer this question, you’ll need to look into the Protocol field of the IP datagram containing this UDP segment (see Figure 4.13 in the text, and the discussion of IP header fields).
```sh
Check #5 
```
7. Examine the pair of UDP packets in which your host sends the first UDP packet and the second UDP packet is a reply to this first UDP packet. (Hint: for a second packet to be sent in response to a first packet, the sender of the first packet should be the destination of the second packet). What is the packet number5 of the first of these two UDP segments in the trace file? What is the value in the source port field in this UDP segment? What is the value in the destination port field in this UDP segment? What is the packet number6 of the second of these two UDP segments in the trace file? What is the value in the source port field in this second UDP segment? What is the value in the destination port field in this second UDP segment? Describe the relationship between the port numbers in the two packets.
```sh
Packet number of the first of these 2 UDP segments: 5
Value in the source port field: 47931 
Valie in the dest port field: 1900 
Packet number of the second:  6
Value in the src port field in the 2nd: 47931 
Value in the dest port field in the 2nd: 1900

The relationship: (?)
```