import re


def check_suspicious_url(url):
    # Check for IP address in URL
    ip_pattern = re.compile(r'^(?:http|ftp)s?://' # http:// or https:// or ftp:// or ftps://
                            r'(?:(?:[0-9]{1,3}.){3}[0-9]{1,3}' # IP address like 192.168.0.1
                            r'|' # or
                            r'(?:www.|[^.]+.)(?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|pro|tel|travel|xxx|[a-z]{2})\b/?)') # domain name
    if ip_pattern.match(url):
        return True

    # Check for deceptive URLs
    deceptive_pattern = re.compile(r'^https?://[a-zA-Z0-9-.]+(.|-)+[a-zA-Z0-9-.]+/')
    if deceptive_pattern.match(url):
        return True

    # Check for long URLs
    if len(url) > 75:
        return True

    # Check for URL shortening services
    url_shorteners = ['bit.ly', 'goo.gl', 't.co', 'tinyurl.com', 'ow.ly', 'buff.ly', 'is.gd', 'clck.ru', 'adf.ly', 'j.mp', 'fb.me', 'v.gd', 's.id', 's.id', 'x.co', 't2m.io', 'tiny.cc', 'lnkd.in', 'po.st', 'qr.ae']
    for shortener in url_shorteners:
        if shortener in url:
            return True

    # Check for homograph attacks
    homograph_pattern = re.compile(r'^https?://[\w-.]+([^\w-.]|\b)-[\w-.]+.[\w-.]{2,}')
    if homograph_pattern.match(url):
        return True

    return False

url = 'https://www.google.com/'
is_suspicious = check_suspicious_url(url)
print(is_suspicious)