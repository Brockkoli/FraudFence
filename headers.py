import colorama
import requests


def headers(url):
    colorama.init()
    
    try:
        if url.startswith("https://"):
                url = url.strip("https://")
        elif url.startswith("http://"):
                url = url.strip("http://")
        elif url.startswith("www"):     
                url = url.strip("www")
        elif url.startswith("https://www"):     
                url = url.strip("https://www")
        elif url.startswith("http://www"):     
                url = url.strip("http://www")
        url = "https://www." + url

        print("Header of: " + colorama.Fore.YELLOW + url + colorama.Style.RESET_ALL)
        print("-" * 50)

        response = requests.head(url)
        headers = response.headers

        for header, value in headers.items():
            # the Content-Security-Policy header displays all the browsers in one line
            if header == "Content-Security-Policy":
                # the join function will print each output in one line
                value = ', \n'.join(value.split())
            print(f"{colorama.Fore.GREEN + header + colorama.Style.RESET_ALL}: {value}")
        print("-" * 50)

        checker = input("Do you wish to continue? (Y/N) ")
        if checker == "y":
            return True
        else:
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
