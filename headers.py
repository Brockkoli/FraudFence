import colorama
import requests


def headers(url):
    colorama.init()
    print(colorama.Fore.YELLOW + "*" * 50 + colorama.Style.RESET_ALL)

    try:
        if not url.startswith("http"):
            url = "https://" + url
        response = requests.head(url)
        headers = response.headers

        for header, value in headers.items():
            # the Content-Security-Policy header displays all the browsers in one line
            if header == "Content-Security-Policy":
                # the join function will print each output in one line
                value = ', \n'.join(value.split())
            print(f"{colorama.Fore.GREEN + header + colorama.Style.RESET_ALL}: {value}")
        print(colorama.Fore.YELLOW + "*" * 50 + colorama.Style.RESET_ALL)

        checker = input("Do you wish to continue? (Y/N) ")
        if checker == "y":
            return True
        else:
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
