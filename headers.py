import colorama
import requests


def headers(url):
    colorama.init()
    
    try:
        if url.startswith("https://www"):
            url = url.replace("https://www.", "", 1)
        elif url.startswith("http://www"):
            url = url.replace("http://www.", "", 1)
        elif url.startswith("https://"):
            url = url.replace("https://", "", 1)
        elif url.startswith("http://"):
            url = url.strip("http://")
        elif url.startswith("www"):     
            url = url.strip("www")
        elif url.startswith("http://www"):     
            url = url.strip("http://www")
        url = "https://www." + url

        print("Header of: " + colorama.Fore.YELLOW + url + colorama.Style.RESET_ALL)
        print("-" * 50)

        response = requests.head(url)
        headers = response.headers

        headers_dict = {}

        for header, value in headers.items():
            # the Content-Security-Policy header displays all the browsers in one line
            if header == "Content-Security-Policy":
                # the join function will print each output in one line
                value = ', \n'.join(value.split())

            headers_dict[header] = value
            print(f"{colorama.Fore.GREEN + header + colorama.Style.RESET_ALL}: {value}")

        print("-" * 50)
        return headers_dict
    except requests.exceptions.RequestException as e:
        # print(f"Error: {e}")
        print("No headers found.\n")
