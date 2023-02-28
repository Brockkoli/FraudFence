import ssl
import socket
from urllib.parse import urlparse

def url_checker(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

url = input("Enter website URL: ")
if not url_checker(url):
    print("Invalid URL. Please enter a valid URL including the scheme (e.g. https://www.example.com)")
    exit()

url_name = url.split('//')[1].split('/')[0]

try:
    context = ssl.create_default_context()
    with socket.create_connection((url_name, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=url_name) as ssock:
            cert = ssock.getpeercert()
            for key, value in cert.items():
                print(f"{key}: {value}")
except Exception as e:
    print(f"Error: {e}")
