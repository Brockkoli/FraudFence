import socket
import ssl
import re
import colorama
import textwrap

colorama.init()


def print_cert_info(cert: dict):
    rows = []
    for key, value in cert.items():
        str_value = str(value)
        str_value = re.sub(r'[(),]', '', str_value)
        rows.append([key, str_value])

    max_key_length = max(len(row[0]) for row in rows)

    print(colorama.Fore.GREEN + f"{'Headers':<{max_key_length}} | Information" + colorama.Style.RESET_ALL)
    print("-" * (max_key_length + 1) + "|" + "-" * 50)

    for row in rows:
        key = row[0]
        value = row[1]
        wrapped_values = textwrap.wrap(value, width=50, initial_indent=" " * 0, subsequent_indent=" " * 0)

        print(colorama.Fore.YELLOW + f"{key:<{max_key_length}}" + colorama.Style.RESET_ALL + f" | {wrapped_values[0]}")

        for line in wrapped_values[1:]:
            print(" " * (max_key_length + 3) + line)


def ssl_checker(url):
    if url.startswith("https://www."):     
        url = url.replace("https://www.", "", 1)
    elif url.startswith("http://www."):     
        url = url.replace("http://www.", "", 1)
    elif url.startswith("https://"):
        url = url.replace("https://", "", 1)
    elif url.startswith("http://"):
        url = url.replace("http://", "", 1)
    elif url.startswith("www."):     
        url = url.replace("www.", "", 1)

    print("first: ", url)
    url = "www." + url
    print("second: ", url)

    print("SSL information for the URL: ", colorama.Fore.YELLOW + url + colorama.Style.RESET_ALL)
    print("-" * 66)

    try:
        context = ssl.create_default_context()
        with socket.create_connection((url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssock:
                cert = ssock.getpeercert()
                print_cert_info(cert)
                return cert
        print("-" * 66)

    except Exception as e:
        print(f"Error: {e}")
