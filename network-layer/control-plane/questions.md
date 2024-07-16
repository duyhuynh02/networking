# HOMEWORK QUESTIONS
Questions in the textbook. Decided to answer most of the questions here. 

## Section 5.1

R1. What is meant by a control plane that is based on per-router control? In such cases, when we say the network control and data planes are implemented “monolithically,” what do we mean?
```sh
That means we act, update, and connect the same way. 
```
R2. What is meant by a control plane that is based on logically centralized control? In such cases, are the data plane and the control plane implemented within the same device or in separate devices? Explain.
```sh
Data plane is used for routing 
Control plane is used for forwarding 

When it's based on logically centralized control, it' still in a routing step, so the data and control plane do not implement in within the same device.  
```

## Section 5.2
R3. Compare and contrast the properties of a centralized and a distributed routing algorithm. Give an example of a routing protocol that takes a centralized and a decentralized approach.

| Centralized routing | Distributed routing |
|-------------|-------------------------------|
|Managed by only singler center node | Can make their own decisions| 
|Optimize routing decisions based on global knowledege | Faster decision making and no single point of failure |

R4. Compare and contrast static and dynamic routing algorithms.

| Static routing | Dynamic routing  |
|-------------|---------------------|
|Manually configure routing entries | Adapts to the network automatically

R5. What is the “count to infinity” problem in distance vector routing?
```sh
When two nodes use the misinformation (by one node delete the link and does not inform the neighbor yet)
```
R6. How is a least cost path calculated in a decentralized routing algorithm?
```sh
By update itself and inform the cost to the neighbors
```

