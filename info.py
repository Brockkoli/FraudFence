import requests
from bs4 import BeautifulSoup
from whois import whois
import datetime

# make a request to the website
url = "https://www.google.com"
response = requests.get(url)

# check the status code of the response
if response.status_code == 200:
    # parse the HTML content of the website
    soup = BeautifulSoup(response.content, "html.parser")

    # get the title of the website
    title = soup.title.string
    print("Title:", title)

    # get the description of the website
    description = soup.find("meta", attrs={"name": "description"})
    if description:
        print("Description:", description["content"])

    # get the WHOIS information of the website
    domain = url.split("//")[-1].split("/")[0]
    whois_info = whois(domain)
    print("Registrar:", whois_info.registrar)
    creation_date = [date.strftime('%d-%B-%Y') for date in whois_info.creation_date]
    expiration_date = [date.strftime('%d-%B-%Y') for date in whois_info.expiration_date]
    print("Creation Date:", creation_date)
    print("Expiration Date:", expiration_date)
else:
    print("Error:", response.status_code)
    
