# PROBLEMS
I decide to work on problems which I found interesting and challenging. The full set of problems you can find and check on the textbook. Please buy a digital/hardcover to support the teachers. This solution is for educational purpose only.

## SOLUTIONS 
![alt text](P3.png)

| step | N' | D(z), p(z) | D(y), p(y)| D(v), p(v)| D(w), p(w)| D(t), p(t) | D(u), p(u) |
|------|----|-------------|-----------|-----------|------------|------------|-----------|
| 0 | x | 8, x | 6, x | 3, x | 6, x | ∞ | ∞
| 1 | xv | 8, x | 6,x |  | 6, x | 7, v | 6, v 
| 2 | xvu | 8, x | 6, x | | 6, x | 6, v | 
| 3 | xvuw | 8, x | 6, x | | | 6, v| | |
| 4 | xvuwt | 8, x | 6, x | | | | | 
| 5 | xvuwty | 8 , x | |  | | | | 
| 6 | xvuwtyz  

![alt text](P5.png)


Step 0: 
|   | u | v | y | x | z |
|---|---|---|---|---|---|
| u | ∞ | ∞ | ∞ | ∞ | ∞ |
| v | ∞ | 3 | ∞ | ∞ | ∞ |
| y | ∞ | ∞ | ∞ | ∞ | ∞ |
| x | ∞ | ∞ | ∞ | 2 | ∞ |
| z | ∞ | ∞ | ∞ | ∞ | 0 |

Step 1: Distance vector of v: D(v) = {u:2, y:4, x:1, z:3}
Update table using: 
D(z, u) = min()
D(z, y) = 
D(z, x) = 
D(z, v) = 
|   | u | v | y | x | z |
|---|---|---|---|---|---|
| u | ∞ | ∞ | ∞ | ∞ | ∞ |
| v | ∞ | 3 | ∞ | ∞ | ∞ |
| y | ∞ | ∞ | ∞ | ∞ | ∞ |
| x | ∞ | ∞ | ∞ | 2 | ∞ |
| z | ∞ | ∞ | ∞ | ∞ | 0 |

(LATER)

P6. Consider a general topology (that is, not the specific network shown above) and a synchronous version of the distance-vector algorithm. Suppose that at each iteration, a node exchanges its distance vectors with its neighbors and receives their
distance vectors. Assuming that the algorithm begins with each node knowing
only the costs to its immediate neighbors, what is the maximum number of iterations required before the distributed algorithm converges? Justify your answer.
```sh
n nodes -> n - 1 iterations. 
```

![alt text](figure5-6.png)

P8. Consider the three-node topology shown in Figure 5.6. Rather than having the link costs shown in Figure 5.6, the link costs are c(x,y) = 3, c(y,z) = 6, c(z,x) = 4. Compute the distance tables after the initialization step and after each iteration of a synchronous version of the distance-vector algorithm (as we did in our earlier discussion of Figure 5.6).
```sh
Init table: 

1. Node x table
    x	y	z
x	0	3	4
y	∞	∞	∞
z	∞	∞	∞

1. Node y table
	x	y	z
x	∞	∞	∞
y	3	0	6
z	∞	∞	∞

1. Node z table
	x	y	z
x	∞	∞	∞
y	∞	∞	∞
z	4	6	0
```
```sh
After 1st iteration: 
2. Node x table 
    x	y	z
x	0	3	4
y	3	0	6
z	4	6	0

2. Node y table
	x	y	z
x	0	3	4
y	3	0	6
z	4	6	0

3. Node z table
    x	y	z
x	0	3	4
y	3	0	6
z	4   6   0 		
```

And so on. 
