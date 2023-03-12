import colorama
import dns.resolver

def dnslookup(domain):
    if domain.startswith("https://www"):
        domain = domain.replace("https://www.", "", 1)
    elif domain.startswith("http://www"):
        domain = domain.replace("http://www.", "", 1)
    elif domain.startswith("https://"):
        domain = domain.replace("https://", "", 1)
    elif domain.startswith("http://"):
        domain = domain.strip("http://")
    elif domain.startswith("www"):
        domain = domain.strip("www")
    elif domain.startswith("http://www"):
        domain = domain.strip("http://www")

    colorama.init()

    dns_records = {}

    print("-" * 50)
    print("DNS lookup for " + colorama.Fore.GREEN + domain + "\n" + colorama.Style.RESET_ALL)

    # get A record
    try:
        A_record = dns.resolver.resolve(domain, 'A')
        dns_records['A'] = []
        for ip in A_record:
            print('A Record:', ip.to_text())
            dns_records['A'].append(ip.to_text())
    except:
        print("No A record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get AAAA record
    try:
        AAAA_record = dns.resolver.resolve(domain, 'AAAA')
        dns_records['AAAA'] = []
        for ip in AAAA_record:
            print('AAAA Record:', ip)
            dns_records['AAAA'].append(ip.to_text())
    except:
        print("No AAAA record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get ANY record
    try:
        ANY_record = dns.resolver.resolve(domain, 'ANY')
        dns_records['ANY'] = []
        for record in ANY_record:
            print('ANY Record:', record)
            dns_records['ANY'].append(record.to_text())
    except:
        print("No ANY record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get CAA record
    try:
        CAA_record = dns.resolver.resolve(domain, 'CAA')
        dns_records['CAA'] = []
        for record in CAA_record:
            print('CAA Record:', record)
            dns_records['CAA'].append(record.to_text())
    except:
        print("No CAA record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get CNAME record
    try:
        CNAME_record = dns.resolver.resolve(domain, 'CNAME')
        dns_records['CNAME'] = []
        for record in CNAME_record:
            print('CNAME Record:', record)
            dns_records['CNAME'].append(record.to_text())
    except:
        print("No CNAME record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get MX record
    try:
        MX_record = dns.resolver.resolve(domain, 'MX')
        dns_records['MX'] = []
        for record in MX_record:
            print('MX Record:', record)
            dns_records['MX'].append(record.to_text())
    except:
        print("No MX record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get NS record
    try:
        NS_record = dns.resolver.resolve(domain, 'NS')
        dns_records['NS'] = []
        for record in NS_record:
            print('NS Record:', record)
            dns_records['NS'].append(record.to_text())
    except:
        print("No NS record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get PTR record
    try:
        PTR_record = dns.resolver.resolve(domain, 'PTR')
        dns_records['PTR'] = []
        for record in PTR_record:
            print('PTR Record:', record)
            dns_records['PTR'].append(record.to_text())
    except:
        print("No PTR record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get SOA record
    try:
        SOA_record = dns.resolver.resolve(domain, 'SOA')
        dns_records['SOA'] = []
        for record in SOA_record:
            print('SOA Record:', record)
            dns_records['SOA'].append(record.to_text())
    except:
        print("No SOA record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get SRV record
    try:
        SRV_record = dns.resolver.resolve(domain, 'SRV')
        dns_records['SRV'] = []
        for record in SRV_record:
            print('SRV Record:', record)
            dns_records['SRV'].append(record.to_text())
    except:
        print("No SRV record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get TXT record
    try:
        TXT_record = dns.resolver.resolve(domain, 'TXT')
        dns_records['TXT'] = []
        for record in TXT_record:
            print('TXT Record:', record)
            dns_records['TXT'].append(record.to_text())
    except:
        print("No TXT record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    return dns_records

