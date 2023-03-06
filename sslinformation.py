import socket
import ssl


def ssl_checker(url):
    if url.startswith("https://" or "http://"):
        url = url.strip("https://")
        url = url.strip("http://")

    if not url.startswith("www."):
            newurl = "www." + url
            url = newurl

    try:
        context = ssl.create_default_context()
        with socket.create_connection((url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssock:
                cert = ssock.getpeercert()
                for key, value in cert.items():
                    print(f"{key}: {value}")

        checker = input("Do you wish to continue? (Y/N) ")
        if checker == "y":
            return True
        else:
            return False
    except Exception as e:
        print(f"Error: {e}")
