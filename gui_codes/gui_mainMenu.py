import PySimpleGUI as sg
from pyfiglet import Figlet
from termcolor import colored
import socket
import asyncio

from gui_dnslookup import dnslookup
from gui_headers import headers
from gui_info import whois_check
from gui_locationchecker import serverlocationchecker
from gui_sslinformation import ssl_checker

# this txt file contains our logo in ASCII characters
f = open('fraudfence.txt', 'r')
# show the logo in the GUI
file_contents = f.read()
f.close()
g = Figlet(font='standard')
figlet_text = colored(g.renderText('FraudFence'), 'green')
url = ''

sg.theme('DarkBlack1')

layout = [
    [sg.Text("  "), sg.Text(file_contents, font=('Courier', 6))],
    [sg.Text("\t\t "), sg.Text("WELCOME TO", font=('Courier', 12))],
    [sg.Text("          "), sg.Text(figlet_text, font=('Courier', 7), text_color='#00ff98')],
    [sg.Text("Enter a URL:", key='urlmsg'), sg.InputText(key='url', size=(39,1))],
    [sg.Text("\t"), sg.Button("ENTER", button_color=('#015000'), size=(9, 1), font=('Helvetica', 11)),
    sg.Text("       "), sg.Button("EXIT", button_color=('#750000'), size=(9, 1), font=('Helvetica', 11))],
    [sg.Text(key='option', visible=False, font=('Helvetica', 9)), sg.Text(font=('Helvetica', 9), key='output', visible=False)],
    [sg.Button("Whois", button_color=('grey25'), visible=False, disabled=True), sg.Text("     ", visible=False, key='gap1'),
    sg.Button("DNS Lookup", button_color=('grey25'), visible=False, disabled=True), sg.Text("     ", visible=False, key='gap2'),
    sg.Button("Server Location Checker", button_color=('grey25'), visible=False, disabled=True)],
    [sg.Text("      ", visible=False, key='gap3'), sg.Button("Web Header Checker", button_color=('grey25'), visible=False, disabled=True),
    sg.Text("      ", visible=False, key='gap4'), sg.Button("SSL Information", button_color=('grey25'), visible=False, disabled=True)],
    [sg.Text("Created by Team BottomFrag", font=('Courier', 7))]
]

window = sg.Window('FraudFence', layout, size=(400, 445))

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "EXIT":
        print('Thank you for using FraudFence. Have a safe Internet experience!')
        break

    if event == "ENTER":
        url = values['url']
        # if url field is empty
        if not url:
            window['option'].update("Please enter a URL", visible=True, text_color='red')
        else:
            # make the buttons/text visible and enabled
            window['urlmsg'].update('Update URL: ')
            window['option'].update("Choose an option to run on:", visible=True, text_color="white")
            window['output'].update(url, visible=True, text_color='yellow')
            window['Whois'].update(visible=True, disabled=False)
            window['gap1'].update(visible=True)
            window['DNS Lookup'].update(visible=True, disabled=False)
            window['gap2'].update(visible=True)
            window['Server Location Checker'].update(visible=True, disabled=False)
            window['gap3'].update(visible=True)
            window['Web Header Checker'].update(visible=True, disabled=False)
            window['gap4'].update(visible=True)
            window['SSL Information'].update(visible=True, disabled=False)
            # resize window to fit all the buttons inside
            window.size = (400,530)

    try:
        if event == "Whois":
            result = whois_check(url)
            if not result:
                break
        elif event == "DNS Lookup":
            result = dnslookup(url)
            if not result:
                break
        elif event == "Server Location Checker":
            url = url.strip("https://")
            url = url.strip("http://")
            ip_address = socket.gethostbyname(url)
            result = serverlocationchecker(ip_address)
            if not result:
                break
        elif event == "Web Header Checker":
            result = headers(url)
            if not result:
                break
        elif event == "SSL Information":
            result = ssl_checker(url)
            if not result:
                break
        else:
            continue

    except KeyboardInterrupt:
        print("\nExiting program...")
        break

    except Exception as e:
        print(e)
