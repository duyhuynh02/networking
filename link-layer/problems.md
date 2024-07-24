# PROBLEMS
I decide to work on problems which I found interesting and challenging. The full set of problems you can find and check on the textbook. Please buy a digital/hardcover to support the teachers. This solution is for educational purpose only.

## SOLUTIONS 
P1. Suppose the information content of a packet is the bit pattern 1010 0111 0101 1001 and an even parity scheme is being used. What would the value of the field containing the parity bits be for the case of a two-dimensional parity scheme? Your answer should be such that a minimum-length checksum field is used.
```sh
1 0 1 0 | 0
0 1 1 1 | 1 
0 1 0 1 | 0
1 0 0 1 | 0
- - - - - -
0 0 0 1 | 0
```

```sh
1. Calculate the parity for each row:
Row 1: Even parity (1 + 0 + 1 + 0 = 2, which is even)
Row 2: Even parity (0 + 1 + 1 + 1 = 3, which is odd)
Row 3: Even parity (0 + 1 + 0 + 1 = 2, which is even)
Row 4: Even parity (1 + 0 + 0 + 1 = 2, which is even)

2. Calculate the parity for each column:
Column 1: Even parity (1 + 0 + 0 + 1 = 2, which is even)
Column 2: Even parity (0 + 1 + 1 + 0 = 2, which is even)
Column 3: Even parity (1 + 1 + 0 + 0 = 2, which is even)
Column 4: Even parity (0 + 1 + 1 + 1 = 3, which is odd)

3. Then we combie the row and column parities to get the checksum: 0100 0001 0 
```

P2. For the two-dimensional parity check matrix below, show that:
```sh
0 1 0 1 | 0
1 0 1 0 | 0
0 1 0 1 | 0
1 0 1 0 | 0 
- - - - - - 
0 0 0 0 | 0 

```
a. a single-bit error that can be corrected.
```
Assume we change the bit of position (2, 3), then it becomes:
0 1 0 1 | 0
1 0 0 0 | 1
0 1 0 1 | 0
1 0 1 0 | 0 
- - - - - - 
0 0 1 0 | 0 

In this we can see errors in row 2 and column 3 (the sum 1s is not even). 
```

b. a double-bit error that can be detected, but not corrected.
```sh
0 1 0 1 | 0 
1 0 0 0 | 1
0 1 0 0 | 1
1 0 1 0 | 0
- - - - - - 
0 0 1 1 | 0 

In this case, we can detect the error in Row 2, 3 and Column 3, 4. However, these intersect at multiple points: (2, 3), (2, 4), (3, 3), and (3, 4), making it unclear which bits are in error.
```

P3. Suppose the information portion of a packet contains six bytes consisting of the 8-bit unsigned binary ASCII representation of string “CHKSUM”; compute the Internet checksum for this data.
```sh
C -> 67 -> 01000011
H -> 72 -> 01001000
K -> 75 -> 01001011
S -> 83 -> 01010011
U -> 85 -> 01010101
M -> 77 -> 01001101

Sum the ASCII values: 67 + 72 + 75 + 83 + 85 + 77 = 459 -> 11001011 (+1 carry bit) -> 11001100
Then the checksum will be 00110011 
```

P5. Consider the generator, G = 1001, and suppose that D has the value 11000111010. What is the value of R?
```sh
First, we need to append (n(G) = 4 - 1) zeros to data, in this case: 3
So D become -> 11000111010000

Second, use binary divison of the extended data by the generator polynomial G using XOR:
11000111010000 XOR 1001 = 11000111011001
=> this is R(remainder) 
```

P10. Consider two nodes, A and B, that use the slotted ALOHA protocol to contend for a channel. Suppose node A has more data to transmit than node B, and node A’s retransmission probability pA is greater than node B’s retransmission probability, pB.

a. Provide a formula for node A’s average throughput. What is the total efficiency of the protocol with these two nodes?
```sh
node A's average throughput: 
```
b. If pA = 2pB, is node A’s average throughput twice as large as that of node B? Why or why not? If not, how can you choose pA and pB to make that happen?
```sh

```
c. In general, suppose there are N nodes, among which node A has retransmission probability 2p and all other nodes have retransmission probability
```sh

```
p. Provide expressions to compute the average throughputs of node A and of any other node.
```sh

```