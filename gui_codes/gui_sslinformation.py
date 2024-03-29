import socket
import ssl
import re
import textwrap
import PySimpleGUI as sg

def print_cert_info(cert: dict):
    # create an empty list then append to it once the values have been scraped
    rows = []
    for key, value in cert.items():
        str_value = str(value)
        str_value = re.sub(r'[(),]', '', str_value)
        rows.append([key, str_value])

    max_key_length = max(len(row[0]) for row in rows)

    output = ''
    output += f"{'Headers':<{max_key_length}} | Information\n"
    output += "-" * (max_key_length + 1) + "|" + "-" * 50 + "\n"

    for row in rows:
        key = row[0]
        value = row[1]
        wrapped_values = textwrap.wrap(value, width=50, initial_indent=" " * 0, subsequent_indent=" " * 0)

        output += f"{key:<{max_key_length}} | {wrapped_values[0]}\n"

        for line in wrapped_values[1:]:
            output += " " * (max_key_length + 3) + line + "\n"

    return output


def ssl_checker(url):
    if url.startswith("https://" or "http://"):
        # remove the http/https scheme from the url
        url = url.strip("https://")
        url = url.strip("http://")

    if not url.startswith("www."):
        # append the www prefix to the url
        newurl = "www." + url
        url = newurl

    try:
        context = ssl.create_default_context()
        with socket.create_connection((url, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=url) as ssock:
                cert = ssock.getpeercert()
                cert_info = print_cert_info(cert)

        layout = [
            [sg.Multiline(("-" * 50 + f"\nSSL information for the URL: {url}\n\n{cert_info}\n" + "-" * 50),
                          size=(79, 20), font=("Courier", 10), background_color="black", text_color="white")],
            [sg.Text("\t\t\t\t        "), sg.Button("CLOSE WINDOW", button_color='#750000')]
        ]
        window = sg.Window('SSL Checker', layout)

        while True:
            event, values = window.read()
            # clicking 'CLOSE WINDOW' or the x button
            if event == sg.WIN_CLOSED or event == "CLOSE WINDOW":
                # close this window and go back to main menu
                window.close()
                return True

    except Exception as e:
        sg.popup(f"Error: {e}")
