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
from tracer import traceroute
from directory import directory
from printalloptions import printall
from ratingcheck import wrr_check

import asyncio
import colorama

colorama.init()

f = open('fraudfence.txt', 'r')
file_contents = f.read()
print(file_contents)
f.close()
g = Figlet(font='standard')
print(colored(g.renderText('     FraudFence'), 'green'))
url = input("Type in the URL: ")

fraudFence = True


def printoptions():
    print("\nHere are some options you can perform on: " + colorama.Fore.YELLOW + "\n" + url + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "*" * 50 + colorama.Style.RESET_ALL)
    print("U. Update URL")
    print("1. Whois")
    print("2. Port Scan")
    print("3. DNS Lookup")
    print("4. Server Location Checker")
    print("5. Web Header Checker")
    print("6. SSL Information")
    print("7. Trace Route")
    print("8. Directory Busting")
    print("9. Web Risk Rating")
    print("10. Print All")
    print("11. Exit")
    print(colorama.Fore.CYAN + "*" * 50 + colorama.Style.RESET_ALL)


def checkoption():
    checker = input("Do you wish to continue? (Y/N) ")
    checkState = True
    if checker.lower() == "y":
        return checkState
    elif checker.lower() == "n":
        checkState = False
        print(checkState)
        return checkState
    else:
        if checker.lower() != "y" or "n":
            print("\nInvalid input. Please enter Y/N. \n")
            checkoption()


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
            elif fraudFence == "1":
                result = whois_check(url)
                checker = checkoption()
                if checker == False:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "2":
                result = portscan_check(url)
                checker = checkoption()
                if checker == False:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "3":
                result = dnslookup(url)
                checker = checkoption()
                if checker == False:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "4":
                url = url.strip("https://")
                url = url.strip("http://")
                ip_address = socket.gethostbyname(url)
                result = serverlocationchecker(ip_address)
                checker = checkoption()
                if checker == False:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "5":
                result = headers(url)
                checker = checkoption()
                if checker == False:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "6":
                result = ssl_checker(url)
                checker = checkoption()
                if checker == False:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "7":
                result = traceroute(url)
                checker = checkoption()
                if checker == False:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "8":
                result = asyncio.run(directory(url))
                checker = checkoption()
                if checker == False:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "9":
                result = wrr_check(url)
                checker = checkoption()
                if checker == False:
                    fraudFence = None
                    exitoption()
            elif fraudFence == "10":
                result = ssl_checker(url)
                result2 = headers(url)
                printall(url,result,result2)
            elif fraudFence == "11":
                fraudFence = None
                exitoption()
            else:
                print("\nInvalid input. Please enter a number between 1 and 11\n")

        except KeyboardInterrupt:
            print("\nExiting program...")
            exit()
