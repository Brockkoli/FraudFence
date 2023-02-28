import requests

url = input("Enter website URL: ")

try:
    response = requests.head(url)
    headers = response.headers

    for header, value in headers.items():
        print(f"{header}: {value}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
