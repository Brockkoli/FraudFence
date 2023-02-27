import dns.resolver

domain = "www.google.com"

# get A record
A_record = dns.resolver.query(domain, 'A')
for ip in A_record:
    print('A Record:', ip)

# get AAAA record
AAAA_record = dns.resolver.query(domain, 'AAAA')
for ip in AAAA_record:
    print('AAAA Record:', ip)

# get ANY record
ANY_record = dns.resolver.query(domain, 'ANY')
for record in ANY_record:
    print('ANY Record:', record)

# get CAA record
CAA_record = dns.resolver.query(domain, 'CAA')
for record in CAA_record:
    print('CAA Record:', record)

# get CNAME record
CNAME_record = dns.resolver.query(domain, 'CNAME')
for record in CNAME_record:
    print('CNAME Record:', record)

# get MX record
MX_record = dns.resolver.query(domain, 'MX')
for record in MX_record:
    print('MX Record:', record)

# get NS record
NS_record = dns.resolver.query(domain, 'NS')
for record in NS_record:
    print('NS Record:', record)

# get TXT record
TXT_record = dns.resolver.query(domain, 'TXT')
for record in TXT_record:
    print('TXT Record:', record)
