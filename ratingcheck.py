import requests
from prettytable import PrettyTable


def wrr_check(t):
    url = "https://wot-web-risk-and-safe-browsing.p.rapidapi.com/targets"

    querystring = {"t": t}

    headers = {
        "X-RapidAPI-Key": "cc25bebdb7msha2bdd052afe2a46p12d2eajsn49f67df7252c",
        "X-RapidAPI-Host": "wot-web-risk-and-safe-browsing.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # Convert the response to a list of dictionaries
    data = response.json()

    # Extract the information from the first dictionary in the list
    info = data[0]

    # Extract the web risk rating and create table
    safety = info["safety"]
    rating = safety["status"]
    rating_color = ""
    if rating == "SUSPICIOUS":
        rating_color = "\033[91m"  # red
    elif rating == "SAFE":
        rating_color = "\033[92m"  # green
    else:
        rating_color = "\033[0m"  # default color

    # Create the table object and set the style
    table = PrettyTable(["Headers", "Web Risk Rating"])
    table.align["Website"] = "l"
    table.align["Web Risk Rating"] = "l"
    table.header_style = "upper"
    table.border = True

    # Set the URL cell text color to yellow
    url_cell = "\033[33m{}\033[0m".format(querystring['t'])

    # Add the URL and rating to the table
    rating_cell = "{}{}\033[0m".format(rating_color, rating)

    table.add_row([url_cell, rating_cell])

    # Extract the categories and add them to table
    categories = info["categories"]
    for category in categories:
        name = category["name"]
        confidence = category["confidence"]
        table.add_row([name, confidence])

    print(table)
    checker = input("Do you wish to continue? (Y/N) ")
    if checker == "y":
        return True
    else:
        return False