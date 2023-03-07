import requests
import xml.dom.minidom
import xml.etree.ElementTree as ET
import colorama

colorama.init()

def whois_check(domain):
        url = "https://whoisapi-whois-v2-v1.p.rapidapi.com/whoisserver/WhoisService"
        # domain = input("Enter the URL domain: ")

        if domain.startswith("https://"):
                domain = domain.strip("https://")
        elif domain.startswith("http://"):
                domain = domain.strip("http://")
        elif domain.startswith("www"):     
                domain = domain.strip("www")
        elif domain.startswith("https://www"):     
                domain = domain.strip("https://www")
        elif domain.startswith("http://www"):     
                domain = domain.strip("http://www")

        querystring = {"domainName":f"{domain}","apiKey":"at_SDpAVjCNg3tXpSyM66qqcKkPyJSTJ","outputFormat":"XML","da":"0","ipwhois":"1","thinWhois":"0","_parse":"0","preferfresh":"0","checkproxydata":"0","ip":"1"}

        headers = {
                "X-RapidAPI-Key": "81c0482df8msh514a1a1beae15f7p1637ccjsnfcaa82735744",
                "X-RapidAPI-Host": "whoisapi-whois-v2-v1.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)

        dom = xml.dom.minidom.parseString(response.text)
        pretty_xml = dom.toprettyxml()

        print("-" * 50)
        print("Whois for: " + colorama.Fore.YELLOW + domain + colorama.Style.RESET_ALL)
        print(pretty_xml)