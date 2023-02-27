import requests
from bs4 import BeautifulSoup
from whois import whois
import colorama

colorama.init()

# make a request to the website
url = "https://www.google.com"
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
    description = soup.find("meta", attrs={"name": "description"})
    if description:
        print("* Description:", description["content"] + "*")
    

    # get the WHOIS information of the website
    domain = url.split("//")[-1].split("/")[0]
    whois_info = whois(domain)
    print("Registrar:", whois_info.registrar)
    print(colorama.Fore.YELLOW + "*" * 30  + colorama.Style.RESET_ALL)
    creation_date = [date.strftime('%d-%B-%Y') for date in whois_info.creation_date]
    expiration_date = [date.strftime('%d-%B-%Y') for date in whois_info.expiration_date]

    # {:<18}" - left-align the string within an 18-character-wide column
    # join() method joins the list elements with a comma and space
    print(colorama.Fore.GREEN + "{:<18} {}".format("Creation Date:", ", ".join(creation_date)))
    print(colorama.Fore.RED + "{:<18} {}".format("Expiration Date:", ", ".join(expiration_date)))
else:
    print("Error:", response.status_code)
    
