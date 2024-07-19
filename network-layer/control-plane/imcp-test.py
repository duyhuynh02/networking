from socket import *
import os
import sys
import struct
import time
import select

ICMP_ECHO_REQUEST = 8

def checksum(source_string):
    """
    A function to calculate the checksum of our packet.
    """
    sum = 0
    count_to = (len(source_string) // 2) * 2
    count = 0

    while count < count_to:
        this = source_string[count + 1] * 256 + source_string[count]
        sum = sum + this
        sum = sum & 0xffffffff
        count = count + 2

    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff

    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer

def receiveOnePing(mySocket, ID, timeout, destAddr):
    timeLeft = timeout
    print('my socket: ', mySocket)
    print('id: ', ID)
    print('timeout: ', timeout)
    print('dest address: ', destAddr)

    while True:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        print('what ready test: ', whatReady)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []:  # Timeout
            return "Request timed out."

        timeReceived = time.time()
        recPacket, addr = mySocket.recvfrom(1024)


        # Fetch the ICMP header from the IP packet
        # icmpHeader = recPacket[20:28]
        # type, code, checksum, packetID, sequence = struct.unpack("bbHHh", icmpHeader)

        # if packetID == ID:
            # bytesInDouble = struct.calcsize("d")
            # timeSent = struct.unpack("d", recPacket[28:28 + bytesInDouble])[0]
            # return timeReceived - timeSent

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <= 0:
            return "Request timed out."

def sendOnePing(mySocket, destAddr, ID):
    """
    Send one ping to the given "destAddr" with the given "ID".
    """
    myChecksum = 0

    # Create a dummy header with a 0 checksum.
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d", time.time())

    # Calculate the checksum on the data and the dummy header.
    myChecksum = checksum(header + data)

    if sys.platform == 'darwin':
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data

    mySocket.sendto(packet, (destAddr, 1))

def doOnePing(destAddr, timeout):
    """
    Perform one ping to the given "destAddr" with the given "timeout".
    """
    icmp = getprotobyname("icmp")
    mySocket = socket(AF_INET, SOCK_RAW, icmp)

    myID = os.getpid() & 0xFFFF  # Return the current process ID
    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)

    mySocket.close()
    return delay

def ping(host, timeout=1):
    """
    Ping a host.
    """
    dest = gethostbyname(host)
    print("Pinging " + dest + " using Python:")
    print("")
    while True:
        delay = doOnePing(dest, timeout)
        print('delay here: ', delay)
        # print(f"Reply from {dest}: time={delay*1000:.2f}ms")
        time.sleep(1)

ping("127.0.0.1")
