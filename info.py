import requests
import xml.dom.minidom
import xml.etree.ElementTree as ET

url = "https://whoisapi-whois-v2-v1.p.rapidapi.com/whoisserver/WhoisService"
domain = input("Enter the URL domain: ")

if domain.startswith("https://" or "http://" or "www"):
        domain = domain.strip("https://")
        domain = domain.strip("http://")
        domain = domain.strip("www")

querystring = {"domainName":f"{domain}","apiKey":"at_SDpAVjCNg3tXpSyM66qqcKkPyJSTJ","outputFormat":"XML","da":"0","ipwhois":"1","thinWhois":"0","_parse":"0","preferfresh":"0","checkproxydata":"0","ip":"1"}

headers = {
	"X-RapidAPI-Key": "81c0482df8msh514a1a1beae15f7p1637ccjsnfcaa82735744",
	"X-RapidAPI-Host": "whoisapi-whois-v2-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

dom = xml.dom.minidom.parseString(response.text)
pretty_xml = dom.toprettyxml()

print(pretty_xml)