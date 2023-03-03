from pyfiglet import Figlet
from termcolor import colored

fraudFence = True
while fraudFence:
    #must change directory FOR NOW
    f = open('fraudfence.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()
    g = Figlet(font = 'standard')
    print(colored(g.renderText('     FraudFence'),'green'))
    print("Welcome to Fraudfence. Here are some options you can perform")
    print("\n1. Whois")
    print("2. Port Scan")
    print("3. DNS Lookup")
    print("4. Server Location Checker")
    print("5. Web Header Checker")
    print("6. SSL Information")
    print("7. exit")

    try:
      fraudFence = input("Choose an option to run: ")
      if fraudFence == "1":
        from info import whois_check #need to change the import
        print("\nperforming Whois...\n")
      elif fraudFence == "2":
        from portscan import portscan_check #need to change the import
        print("\nperforming Port Scan...\n")
      elif fraudFence == "3":
        from dnslookup import dnslookup #need to change the import
        print("\nperforming DNS Lookup...\n")
      elif fraudFence == "4":
        from locationchecker import serverlocationchecker
        print("\nperforming Server Location Checker...\n")
      elif fraudFence == "5":
        from headers import headers
        print("\nperforming Web Header Checker...\n")
      elif fraudFence == "6":
        from sslinformation import ssl_checker
        print("\nperforming SSL Information...\n")
      elif fraudFence == "7":
        print("\nThank you for using FraudFence and have a safe Internet experience!") 
        fraudFence = None
      else:
        print("\nInvalid input. Please enter a number between 1 and 7\n")
    except KeyboardInterrupt:
        print("\nExiting program...")
        exit()
