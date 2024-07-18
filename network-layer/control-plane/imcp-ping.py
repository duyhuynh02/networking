from socket import *
import os
import sys
import struct
import time
import select

ICMP_ECHO_REQUEST = 8

def checksum(source_string):
    csum = 0
    countTo = (len(source_string) // 2) * 2
    count = 0

    while count < countTo:
        thisVal = ord(source_string[count+1]) * 256 + ord(source_string[count])
        csum = csum + thisVal
        csum = csum & 0xffffffff
        count = count + 2

        if countTo < len(source_string):
            csum = csum + ord(source_string[len(source_string) - 1])
            csum = csum & 0xffffffff
        
        csum = (csum >> 16) + (csum & 0xffff)
        csum = csum + (csum >> 16)
        answer = ~csum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer
    
def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout
    
    while 1:
        startedSelect = time.time()         #record a current time, use to measure how long the select call takes 
        whatReady = select.select([mySocket], [], [], timeLeft) #use to monitor the socket for incoming data
        #1st arg: list of sockets to monitor for readability
        #2nd arg: list of sockets to monitor for writability
        #3rd arg: list of sockets for exceptional conditions
        #4th arg: timeout 
        #will return for whatReady 3 lists: first list contains the sockets which are ready for reading 
        #2nd list contains the socket that ready for writing
        #3rd list contain the socket with exceptional conditions 
        print('what ready: ', whatReady)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []: # Timeout
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)

        #Fill in start



        #Fetch the ICMP header from the IP packet
        icmp_header = recPacket[160:192]
        print('imcp_header: ', icmp_header)

        type_, code, checksum, packet_id, sequence = struct.unpack("!bbHHh", icmp_header)
        print(f"ICMP Type: {type_}")
        print(f"ICMP Code: {code}")
        print(f"Checksum: {checksum}")
        print(f"Packet ID: {packet_id}")
        print(f"Sequence: {sequence}")


        #Fill in end
        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return "Request timed out."
            
def sendOnePing(mySocket, destAddr, ID):
    """
    Constructs an IMCP echo request message, compute the checksum, create an actual payoad,
    then send to a specified destination using the provided socket
    """
    # Header is type (8), code (8), checksum (16), id (16), sequence (16)
    myChecksum = 0
    # Make a dummy header with a 0 checksum
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)  
    data = struct.pack("d", time.time())
    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(str(header + data))


    # Get the right checksum, and put in the header
    if sys.platform == 'darwin':
    # Convert 16-bit integers from host to network byte order
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)
    
    
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data


    mySocket.sendto(packet, (destAddr, 1)) # AF_INET address must be tuple, not str
    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object.

def doOnePing(destAddr, timeout):
    """
    Construct then sending the imcp echo request to specified destination address 
    then wait for the reply, calculate the RTT then return the delay 
    """
    icmp = getprotobyname("icmp")
    # SOCK_RAW is a powerful socket type. For more details: http://sockraw.org/papers/sock_raw
    mySocket = socket(AF_INET, SOCK_RAW, icmp)  #ipV4, raw socket and imcp protocol 
    #Raw socket allow direct sending and receiving of network packets

    myID = os.getpid() & 0xFFFF # Return the current process i
    sendOnePing(mySocket, destAddr, myID)   #construct and send an IMCP echo request (ping) packet to specified destination address 
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)

    mySocket.close()
    return delay

def ping(host, timeout=1):
    # timeout=1 means: If one second goes by without a reply from the server,
    # the client assumes that either the client's ping or the server's pong is lost
    dest = gethostbyname(host)
    print("Pinging " + dest + " using Python:")
    print("")
    # Send ping requests to a server separated by approximately one second
    while 1 :
        delay = doOnePing(dest, timeout)
        print('delay here: ', delay)
        time.sleep(1)# one second
    return delay
    
ping("127.0.0.1")