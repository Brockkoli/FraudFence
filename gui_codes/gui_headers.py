import PySimpleGUI as sg
import requests

def headers(url):
    try:
        # strip all possible http/https.www combinations
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

        header_str = "-" * 50 + f"\nHeader of: {url}\n"
        headers_output = [header_str]

        response = requests.head(url)
        headers = response.headers

        for header, value in headers.items():
            if header == "Content-Security-Policy":
                value = ', \n'.join(value.split())
            headers_output.append(f"{header}: {value}")

        headers_output.append("-" * 50)
        headers_output.append("Do you wish to continue? (Y/N) ")

        layout = [[sg.Multiline(default_text="\n".join(headers_output), size=(70, 20), key='OUTPUT', font=("Courier", 10),
                                background_color="black", text_color="white")],
                  [sg.Button("Yes"), sg.Button("No")]
                  ]
        sg.theme("DarkBlack1")

        window = sg.Window("Headers", layout)

        while True:
            event, values = window.read()

            if event == sg.WIN_CLOSED or event == "No":
                return False
            else:
                window.close()
                return True

        window.close()

    except requests.exceptions.RequestException as e:
        sg.popup_error(f"Error: {e}")

