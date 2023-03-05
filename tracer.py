import socket
from scapy.all import *


def traceroute(target):
    ttl = 1
    print("{:<5} {:<20} {:<30} {:<10}".format("TTL", "IP Address", "Hostname", "RTT (ms)"))
    while True:
        # Create an IP packet with the destination and TTL values
        packet = IP(dst=target, ttl=ttl) / ICMP()

        # Send the packet and wait for a response
        reply = sr1(packet, verbose=0, timeout=5)
        # no reply
        if not reply:
            break
        # reply is an ICMP echo reply
        if reply.type == 0:
            print("{:<5} {:<20} {:<30} {:<10.4f}".format(ttl, reply.src, resolve(reply.src), reply.time))
            break
        #  reply is an ICMP time exceeded message
        else:
            print("{:<5} {:<20} {:<30} {:<10.4f}".format(ttl, reply.src, resolve(reply.src), reply.time))
        ttl += 1


def resolve(ip_addr):
    # resolve IP address to hostname
    try:
        return socket.gethostbyaddr(ip_addr)[0]
    except socket.herror:
        return ip_addr


if __name__ == "__main__":
    target = input("Enter target URL or IP address: ")

    # Remove "http://" or "https://://"
    target = target.strip("https://")
    target = target.strip("http://")

    # Remove "www."
    target = target.strip("www.")

    traceroute(target)