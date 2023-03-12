import concurrent.futures
import datetime
import socket
import threading

import colorama

def conversion_url(url):
    if url.startswith("https://"):
        url = url.replace("https://", "", 1)
    elif url.startswith("http://"):
        url = url.replace("http://", "", 1)
    ip_address = socket.gethostbyname(url)
    return ip_address
def portscan_check(url):
    colorama.init()
    results = {}

    # Use conversion_url function to get the IP address of the server
    ip = conversion_url(url)
    portno = input("Type the different types of option you want to run: (default | full | range ( eg: 1-80) )")

    # top 1000 most popular ports in list
    if portno == "default":
        portno = 1
        with open("1000port.txt", "r") as file:
            # read file content into a string var
            portlist = file.read()

    # all ports 1 to 65535
    elif portno == "full":
        first = 1
        last = 65535

    # custom range
    else:
        first, last = portno.split("-")
        first = int(first)
        last = int(last)

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
    def scan(ip, port):
        scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        scanner.settimeout(1)

        try:
            scanresult = scanner.connect_ex((ip, port))
            scanner.close()

            # only one thread can access print output oaat
            with print_lock:

                # open ports
                if scanresult == 0:
                    print(colorama.Fore.GREEN + "{}\t\t{}\t\tOpen".format(ipAddr, port) + colorama.Style.RESET_ALL)
                    results[port] = "Open"

                # closed ports
                else:
                    print(colorama.Fore.RED + "{}\t\t{}\t\tClosed".format(ipAddr, port) + colorama.Style.RESET_ALL)
                    results[port] = "Closed"
        except KeyboardInterrupt:
            print("Exiting program...")

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
            for port in range(first-1, last):
                executor.submit(scan, ip, port + 1)

    print("\nScan finished at:\t {}".format(date_time()))
    print("-" * 60)
    
    sorted_results = sorted(results.items(), key=lambda x: ("Open" not in x[1], x[0]))
    return dict(sorted_results)
