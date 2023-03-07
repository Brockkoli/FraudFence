import colorama
import dns.resolver


def dnslookup(domain):
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

    colorama.init()

    print("-" * 50)
    print("DNS lookup for " + colorama.Fore.GREEN + domain + "\n" + colorama.Style.RESET_ALL)

    # get A record
    try:
        A_record = dns.resolver.resolve(domain, 'A')
        for ip in A_record:
            print('A Record:', ip.to_text())
    except:
        print("No A record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get AAAA record
    try:
        AAAA_record = dns.resolver.resolve(domain, 'AAAA')
        for ip in AAAA_record:
            print('AAAA Record:', ip)
    except:
        print("No AAAA record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get ANY record
    try:
        ANY_record = dns.resolver.resolve(domain, 'ANY')
        for record in ANY_record:
            print('ANY Record:', record)
    except:
        print("No ANY record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get CAA record
    try:
        CAA_record = dns.resolver.resolve(domain, 'CAA')
        for record in CAA_record:
            print('CAA Record:', record)
    except:
        print("No CAA record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get CNAME record
    try:
        CNAME_record = dns.resolver.resolve(domain, 'CNAME')
        for record in CNAME_record:
            print('CNAME Record:', record)
    except:
        print("No CNAME record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get MX record
    try:
        MX_record = dns.resolver.resolve(domain, 'MX')
        for record in MX_record:
            print('MX Record:', record)
    except:
        print("No MX record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get NS record
    try:
        NS_record = dns.resolver.resolve(domain, 'NS')
        for record in NS_record:
            print('NS Record:', record)
    except:
        print("No NS record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    # get TXT record
    try:
        TXT_record = dns.resolver.resolve(domain, 'TXT')
        for record in TXT_record:
            print('TXT Record:', record)
    except:
        print("No TXT record found.")

    print(colorama.Fore.YELLOW + "-" * 40 + colorama.Style.RESET_ALL)

    checker = input("Do you wish to continue? (Y/N) ")
    if checker == "y":
        return True
    else:
        return False
