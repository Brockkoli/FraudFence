import colorama
import requests
import xml.etree.ElementTree as ET

def whois_check(domain):
        colorama.init()
        url = "https://whoisapi-whois-v2-v1.p.rapidapi.com/whoisserver/WhoisService"

        if domain.startswith("https://www"):
            domain = domain.replace("https://www.", "", 1)
        elif domain.startswith("http://www"):
            domain = domain.replace("http://www.", "", 1)
        elif domain.startswith("https://"):
            domain = domain.replace("https://", "", 1)
        elif domain.startswith("http://"):
            domain = domain.replace("http://", "", 1)
        elif domain.startswith("www"):     
            domain = domain.replace("www", "", 1)

        querystring = {"domainName":f"{domain}","apiKey":"at_SDpAVjCNg3tXpSyM66qqcKkPyJSTJ","outputFormat":"XML","da":"0","ipwhois":"1","thinWhois":"0","_parse":"0","preferfresh":"0","checkproxydata":"0","ip":"1"}

        headers = {
                "X-RapidAPI-Key": "1451a54239msh9a771e3bcb0b237p16e5dfjsn9841522a43b3",
                "X-RapidAPI-Host": "whoisapi-whois-v2-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        root = ET.fromstring(response.content)
        stripped_text = root.find(".//strippedText").text

        print("WHOIS information on: " + colorama.Fore.YELLOW + domain + colorama.Style.RESET_ALL)
        print("-" * 50)
        print("Whois for: " + domain)
        print(stripped_text)

        # save stripped_text to a dictionary for easier push to html
        whois_info = {}

        for line in stripped_text.split('\n'):
                parts = line.split(':')
                if len(parts) > 1:
                        key = parts[0].strip()
                        value = ':'.join(parts[1:]).strip()
                        if key == "Name Server":
                                # Name Server can have multiple values
                                # this part will put all values under 'Name Server' into one cell in html, separated by a comma
                                if "Name Servers" not in whois_info:
                                        whois_info["Name Servers"] = []
                                whois_info["Name Servers"].append(value)
                        else:
                                whois_info[key] = value

        return whois_info
