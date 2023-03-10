import dns.resolver
import PySimpleGUI as sg

def dnslookup(domain):
    # strip all possible http/https.www combinations
    if domain.startswith("https://"):
        domain = domain.strip("https://")
    elif domain.startswith("http://"):
        domain = domain.strip("http://")
    elif domain.startswith("www"):
        domain = domain.strip("www.")
    elif domain.startswith("https://www"):
        domain = domain.strip("https://www")
    elif domain.startswith("http://www"):
        domain = domain.strip("http://www")

    output = "-" * 50 + "\n" + "DNS lookup for " + domain + "\n" + "\n"

    # get A record
    try:
        A_record = dns.resolver.resolve(domain, 'A')
        for ip in A_record:
            output += 'A Record: ' + ip.to_text() + "\n"
    except:
        output += "No A record found." + "\n"

    output += "-" * 40 + "\n"

    # get AAAA record
    try:
        AAAA_record = dns.resolver.resolve(domain, 'AAAA')
        for ip in AAAA_record:
            output += 'AAAA Record: ' + str(ip) + "\n"
    except:
        output += "No AAAA record found." + "\n"

    output += "-" * 40 + "\n"

    # get ANY record
    try:
        ANY_record = dns.resolver.resolve(domain, 'ANY')
        for record in ANY_record:
            output += 'ANY Record: ' + str(record) + "\n"
    except:
        output += "No ANY record found." + "\n"

    output += "-" * 40 + "\n"

    # get CAA record
    try:
        CAA_record = dns.resolver.resolve(domain, 'CAA')
        for record in CAA_record:
            output += 'CAA Record: ' + str(record) + "\n"
    except:
        output += "No CAA record found." + "\n"

    output += "-" * 40 + "\n"

    # get CNAME record
    try:
        CNAME_record = dns.resolver.resolve(domain, 'CNAME')
        for record in CNAME_record:
            output += 'CNAME Record: ' + str(record) + "\n"
    except:
        output += "No CNAME record found." + "\n"

    output += "-" * 40 + "\n"

    # get MX record
    try:
        MX_record = dns.resolver.resolve(domain, 'MX')
        for record in MX_record:
            output += 'MX Record: ' + str(record) + "\n"
    except:
        output += "No MX record found." + "\n"

    output += "-" * 40 + "\n"

    # get NS record
    try:
        NS_record = dns.resolver.resolve(domain, 'NS')
        for record in NS_record:
            output += 'NS Record: ' + str(record) + "\n"
    except:
        output += "No NS record found." + "\n"

    # get TXT record
    try:
        TXT_record = dns.resolver.resolve(domain, 'TXT')
        for record in TXT_record:
            output += 'TXT Record: ' + str(record) + "\n"
    except:
        output += "No TXT record found." + "\n"

    output += "-" * 50 + "\n" + "Do you wish to continue? (Y/N)"
    layout = [
        [sg.Multiline(output, size=(70, 20), key='-OUTPUT-', autoscroll=True, background_color='black',
                      font=('Courier', 10), text_color='white')],
        [sg.Button('Yes'), sg.Button('No')]
    ]

    window = sg.Window('DNS Lookup', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'No':
            return False
        else:
            window.close()
            return True
