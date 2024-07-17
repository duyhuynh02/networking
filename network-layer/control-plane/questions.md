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

## Sections 5.3–5.4
R7. Why are different inter-AS and intra-AS protocols used in the Internet?
```sh
Inter: Global (international?)
Intra: Local
```
R8. True or false: When an OSPF route sends its link state information, it is sent only to those nodes directly attached neighbors. Explain.
```sh
False. OSPF tried to find the least cost. OSPF propagates all the network.
```
R9. What is meant by an area in an OSPF autonomous system? Why was the concept of an area introduced?
```sh
Due to link state advertisement, the concept of area means directly connected links, interfaces, and neighbors. 
```
R10. Define and contrast the following terms: subnet, prefix, and BGP route.
```sh
Subnet: a sub network 
Prefix: refers to an original IP address which indicate the network segment
BGP route: can be iBGP (use internal) or eBGP (use external) for propagation purpose 
```
R11. How does BGP use the NEXT-HOP attribute? How does it use the AS-PATH attribute?
```sh
NEXT-HOP attribute uses to determine which interface to use for forwarding packets to the specificied destination. 

AS-PATH: indicate a list of AS numbers which the BGP update has already traversed. 
```
R12. Describe how a network administrator of an upper-tier ISP can implement policy when configuring BGP.
```sh
N/A 
```
R13. True or false: When a BGP router receives an advertised path from its neighbor, it must add its own identity to the received path and then send that new path on to all of its neighbors. Explain
```sh
False, it's a policy-based routing protocol so it should be not a restrict to add its own identity... 
```

## SECTION 5.5
R14. Describe the main role of the communication layer, the network-wide state management layer, and the network-control application layer in an SDN controller.
```sh
Communication layer: involved a communication between a SDN controller and controled network devices 
Network-wide state management layer: The control decisisions made by the SDN control plane 
Network-control application layer: interacts with network-control apps, allow to read/write network state and flow tables within the state-management layer 
```

R15. Suppose you wanted to implement a new routing protocol in the SDN control plane. At which layer would you implement that protocol? Explain.
```sh
Network-wide state management layer 
```
R16. What types of messages flow across an SDN controller’s northbound and southbound APIs? Who is the recipient of these messages sent from the controller across the southbound interface, and who sends messages to the controller across the northbound interface?
```sh
Northbound API: from controller to application -> topology info, flow statistics, event notifications, policy update e.g., RESTful API, OpenFlow, NETCONF,...
Southbound API: from controller to network devices -> flow installation, topology discovery, group configuration, port configuration e.g.,, OpenFlow,...
```
R17. Describe the purpose of two types of OpenFlow messages (of your choosing) that are sent from a controlled device to the controller. Describe the purpose of two types of Openflow messages (of your choosing) that are send from the controller to a controlled device.
```sh
Modify-State: add/delete or modify entries values from switch's flow table and ports
Read-state: send a specific packet out of a specified port at the controller switch. 
```
R18. What is the purpose of the service abstraction layer in the OpenDaylight SDN
controller?
```sh
Is controller's nerver center, use for allowing controllers component and application to invoke each's other 
```

## SECTIONs 5.6–5.7
R19. Names four different types of ICMP messages
```sh
0 -> echo reply (to ping)
3 -> based on the code we will have ethe destination 
4 -> source quench (congestion control)
8 -> echo request 
```
R20. What two types of ICMP messages are received at the sending host executing the Traceroute program?
```sh
Type 11 code 0: TTL value 
Type 3 code 3: unreachable destination port 
```
R21. Define the following terms in the context of SNMP: managing server, managed device, network management agent and MIB.
```sh
Managing server: control the collections, process, analyze and dispatch network management information and commands
Managed device: a pice of network equipment e.g., host, router, switch, middlebox, modem,...
Network management agent: software process in a managed device that communicates with the managing server, taking local actions at the managed device under the command and control of the managing server 
MIB: Management information base 
```
R22. What are the purposes of the SNMP GetRequest and SetRequest messages?
```sh
GetRequest: get value of one or more MIB object instances
SetRequest: set value of one or more MIB object instances 
```
R23. What is the purpose of the SNMP trap message?
```sh
Serves as an unsolicited communication trom a network device to an SNMP management system -> allow for proactive monitoring, rapid incident response. 
```