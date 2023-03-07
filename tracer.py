import socket
from scapy.all import *
from scapy.layers.inet import ICMP, IP
import colorama

colorama.init()


def traceroute(target):

    if target.startswith("https://"):
            target = target.strip("https://")
    elif target.startswith("http://"):
            target = target.strip("http://")
    elif target.startswith("www"):     
            target = target.strip("www")
    elif target.startswith("https://www"):     
            target = target.strip("https://www")
    elif target.startswith("http://www"):     
            target = target.strip("http://www")

    ttl = 1

    print("\nTraceroute for: " + colorama.Fore.YELLOW + target + colorama.Style.RESET_ALL)
    print("-" * 50)

    print(colorama.Fore.GREEN + "{:<5} {:<20} {:<30} {:<10}".format("TTL", "IP Address", "Hostname", "RTT (ms)" + colorama.Style.RESET_ALL))
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

    checker = input("Do you wish to continue? (Y/N) ")
    if checker == "y":
        return True
    else:
        return False


def resolve(ip_addr):
    # resolve IP address to hostname
    try:
        return socket.gethostbyaddr(ip_addr)[0]
    except socket.herror:
        return ip_addr
