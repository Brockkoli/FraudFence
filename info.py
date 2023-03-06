import colorama
import requests
from bs4 import BeautifulSoup
from whois import whois


def whois_check(url):
    colorama.init()

    if not url.startswith("http"):
        url = "https://" + url
    response = requests.get(url)

    # check the status code of the response
    if response.status_code == 200:
        # parse the HTML content of the website
        soup = BeautifulSoup(response.content, "html.parser")

        print(colorama.Fore.YELLOW + "*" * 30 + colorama.Style.RESET_ALL)
        # get the title of the website
        title = soup.title.string
        print("Title:", title)

        # get the description of the website
        try:
            description = soup.find("meta", attrs={"name": "description"})
            if description:
                print("Description:", description["content"])
        except:
            print("Closing socket.")

        # get the WHOIS information of the website
        domain = url.split("//")[-1].split("/")[0]
        whois_info = whois(domain)

        print("Registrar:", whois_info.registrar)
        print(colorama.Fore.YELLOW + "*" * 30 + colorama.Style.RESET_ALL)

        if whois_info.creation_date:
            try:
                creation_date = [date.strftime('%d-%B-%Y') for date in whois_info.creation_date]
                print(colorama.Fore.GREEN + "{:<18} {}".format("Creation Date:", ", ".join(creation_date)))
            except:
                creation_date = [whois_info.creation_date.strftime('%d-%B-%Y')]
                # {:<18}" - left-align the string within an 18-character-wide column
                # join() method joins the list elements with a comma and space
                print(colorama.Fore.GREEN + "{:<18} {}".format("Creation Date:", ", ".join(creation_date)))
        else:
            print("Creation date not available.")

        if whois_info.expiration_date:
            try:
                expiration_date = [date.strftime('%d-%B-%Y') for date in whois_info.expiration_date]
                print(colorama.Fore.RED + "{:<18} {}".format("Expiration Date:", ", ".join(expiration_date)))
                print(colorama.Fore.YELLOW + "-" * 30 + colorama.Style.RESET_ALL)
            except:
                expiration_date = [whois_info.expiration_date.strftime('%d-%B-%Y')]
                print(colorama.Fore.RED + "{:<18} {}".format("Expiration Date:", ", ".join(expiration_date)))
                print(colorama.Fore.YELLOW + "-" * 30 + colorama.Style.RESET_ALL)
        else:
            print("Expiration date not available.")

        # Name Servers
        if whois_info.name_servers:
            print("Name Servers:")
            for ns in whois_info.name_servers:
                print("\t", ns)

        print(colorama.Fore.YELLOW + "-" * 30 + colorama.Style.RESET_ALL)

        # Registrant Information
        if whois_info.name:
            print('Registrant name:', whois_info.name)

        if whois_info.email:
            print('Registrant email:', whois_info.email)

        if whois_info.address:
            print('Registrant address:', whois_info.address)

        print(colorama.Fore.YELLOW + "-" * 30 + colorama.Style.RESET_ALL)

        checker = input("Do you wish to continue? (Y/N) ")
        if checker == "y":
            return True
        else:
            return False
    else:
        print("Error:", response.status_code)
