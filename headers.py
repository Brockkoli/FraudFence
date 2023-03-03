import requests
import colorama

colorama.init()

url = input("Enter website URL: ")
print(colorama.Fore.YELLOW + "*" * 50 + colorama.Style.RESET_ALL)

try:
    response = requests.head(url)
    headers = response.headers

    for header, value in headers.items():
        print(f"{colorama.Fore.GREEN + header  + colorama.Style.RESET_ALL}: {value}")
    print(colorama.Fore.YELLOW + "*" * 50 + colorama.Style.RESET_ALL)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")