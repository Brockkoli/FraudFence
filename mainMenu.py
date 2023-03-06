import socket

from pyfiglet import Figlet
from termcolor import colored

# Importing modules
from dnslookup import dnslookup
from headers import headers
from info import whois_check
from locationchecker import serverlocationchecker
from portscan import portscan_check
from sslinformation import ssl_checker

f = open('fraudfence.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()
g = Figlet(font='standard')
print(colored(g.renderText('     FraudFence'), 'green'))
url = input("Type in the URL: ")

fraudFence = True


def printoptions():
    print("Welcome to Fraudfence. Here are some options you can perform on " + url)
    print("\nU. Update URL")
    print("1. Whois")
    print("2. Port Scan")
    print("3. DNS Lookup")
    print("4. Server Location Checker")
    print("5. Web Header Checker")
    print("6. SSL Information")
    print("7. exit\n")


def exitoption():
    if fraudFence is None:
        print("\nThank you for using FraudFence and have a safe Internet experience!")
        exit()


if fraudFence:
    while fraudFence:
        printoptions()
        try:
            fraudFence = input("Choose an option to run: ")
            if fraudFence == "u":
                url = input("Type in the URL: ")
            if fraudFence == "1":
                result = whois_check(url)
                if not result:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "2":
                result = portscan_check(url)
                if not result:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "3":
                result = dnslookup(url)
                if not result:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "4":
                url = url.strip("https://")
                url = url.strip("http://")
                ip_address = socket.gethostbyname(url)
                result = serverlocationchecker(ip_address)
                if not result:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "5":
                result = headers(url)
                if not result:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "6":
                result = ssl_checker(url)
                if not result:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "7":
                fraudFence = None
                exitoption()
            else:
                print("\nInvalid input. Please enter a number between 1 and 7\n")

        except KeyboardInterrupt:
            print("\nExiting program...")
            exit()
