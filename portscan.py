import datetime
import socket
import concurrent.futures
import argparse
import threading

# temporary parser to test port scanning cli, will change at main.py
parser = argparse.ArgumentParser(prog='portscan.py', usage='%(prog)s [Target] [Port]', epilog="Example: python portscan.py 192.168.1.1 1-10000")
parser.add_argument("target", help = "The target IP address or URL")
parser.add_argument("port", help = "The Port Number(s) (default = 1000 most popular port no.)", default=1,  nargs = '?') 

args = parser.parse_args()

ip=args.target
portno=args.port

# top 1000 most popular ports in list
if portno == 1:
    with open("1000port.txt", "r") as file:
        # read file content into a string var
        portlist = file.read()
    
# all ports 1 to 65535
elif portno == "full":
    first=1
    last=65535

# custom range
else:
    first, last= portno.split("-")
    first= int(first)
    last= int(last)

print("*" * 60)
print("PORT SCANNER")
print("*" * 60)

def date_time():
	return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

print_lock = threading.Lock()

# resolves hostname to IP address
ipAddr = socket.gethostbyname(ip)

# Timestamp
print("-" * 60)
print("Scanning Target:\t {}".format(ip, ipAddr))
print("Scan started at:\t {}".format(date_time()))
print("-" * 60)

# Scan function
def scan(ip,port):
    scanner= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    try:
        scanner.connect((ip,port))
        scanner.close()
        with print_lock:
            print("{}\t\t{}\t\tOpen".format(ipAddr, port))
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    # scan ports from txt file
    if portno == 1:
        print("Scanning the 1000 most popular ports...")
        print("*" * 60)
        print("\n      Ip\t\tPort\t\tState")
        print("-" * 60)
        # split txt file content into a list of integers
        ports = [int(x) for x in portlist.split(",")]

        # scan all ports in the list
        for port in ports:
            executor.submit(scan, ip, port)

    else:
        print("Scanning ports...")
        print("*" * 60)
        print("\n      Ip\t\tPort\t\tState")
        print("-" * 60)
        for port in range(first, last):
           executor.submit(scan, ip, port + 1)

print("\nScan finished at:\t {}".format(date_time()))
print("-" * 60)