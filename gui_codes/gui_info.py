import requests
import xml.etree.ElementTree as ET
import PySimpleGUI as sg

def whois_check(domain):
    # using this API to help with the code
    url = "https://whoisapi-whois-v2-v1.p.rapidapi.com/whoisserver/WhoisService"

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

    root = ET.fromstring(response.content)
    stripped_text = "-" * 50 + f"\nWHOIS information on: {domain} \n\n" \
                    + root.find(".//strippedText").text + "-" * 50 \
                    + "\nDo you wish to continue? (Y/N)"

    layout = [[sg.Multiline(stripped_text, key='output', size=(70, 20),
                            background_color="black", text_color="white", font=("Courier", 10))],
              [sg.Button("Yes"), sg.Button("No")]]

    window = sg.Window("WHOIS Lookup", layout, finalize=True)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "No":
            return False
        else:
            window.close()
            return True

    window.close()
