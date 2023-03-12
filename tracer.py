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

    tracer_list = []
    print(colorama.Fore.GREEN + "{:<5} {:<20} {:<30} {:<10}".format("TTL", "IP Address", "Hostname",
                                                                    "RTT (ms)" + colorama.Style.RESET_ALL))
    while True:
        packet = IP(dst=target, ttl=ttl) / ICMP()
        reply = sr1(packet, verbose=0, timeout=5)
        tracer_tuple = ()

        if not reply:
            break

        if reply.type == 0:
            print("{:<5} {:<20} {:<30} {:<10.4f}".format(ttl, reply.src, resolve(reply.src), reply.time))

            # add traceroute info to the list as a dictionary
            tracer_dict = {"TTL": ttl, "IP Address": reply.src, "Hostname": resolve(reply.src), "RTT (ms)": reply.time}
            for key, value in tracer_dict.items():
                tracer_tuple += (value,)
            tracer_list.append(tracer_dict)
            break

        else:
            print("{:<5} {:<20} {:<30} {:<10.4f}".format(ttl, reply.src, resolve(reply.src), reply.time))

            # add traceroute info to the list as a dictionary
            tracer_dict = {"TTL": ttl, "IP Address": reply.src, "Hostname": resolve(reply.src), "RTT (ms)": reply.time}
            for key, value in tracer_dict.items():
                tracer_tuple += (value,)
            tracer_list.append(tracer_dict)

        ttl += 1

    # return the list of traceroute dictionaries
    return tracer_list



def resolve(ip_addr):
    # resolve IP address to hostname
    try:
        return socket.gethostbyaddr(ip_addr)[0]
    except socket.herror:
        return ip_addr
