from pyfiglet import Figlet
from termcolor import colored
fraudFence = True
while fraudFence:
    #must change directory FOR NOW
    f = open('C:\\Users\\Jevan\\Downloads\\fraudfence4.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()
    g = Figlet(font = 'standard')
    print(colored(g.renderText('     FraudFence'),'green'))
    print("Welcome to Fraudfence. Here are some stuff you can do")
    print("\n1. whois")
    print("2. port scan")
    print("3. dns lookup")
    print("4. exit")
    fraudFence = input("Choose an option to run: ")
    if fraudFence == "1":
      print("\nperforming whois...\n")
    elif fraudFence == "2":
      print("\nperforming port scan...\n")
    elif fraudFence == "3":
      print("\nperforming dns lookup...\n")
    elif fraudFence == "4":
      print("\nThank you for using FraudFence and have a safe Internet experience!") 
      fraudFence = None
    else:
       print("\nInvalid input. Please enter a number between 1 and 4\n")