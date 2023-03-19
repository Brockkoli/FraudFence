import requests
from prettytable import PrettyTable


def wrr_check(t):
    url = "https://wot-web-risk-and-safe-browsing.p.rapidapi.com/targets"

    if t.startswith("https://www"):
        t = t.replace("https://www.", "", 1)
    elif t.startswith("http://www"):
        t = t.replace("http://www.", "", 1)
    elif t.startswith("https://"):
        t = t.replace("https://", "", 1)
    elif t.startswith("http://"):
        t = t.replace("http://", "", 1)
    elif t.startswith("www"):     
        t = t.replace("www", "", 1)
        
    querystring = {"t": t}

    headers = {
        "X-RapidAPI-Key": "1451a54239msh9a771e3bcb0b237p16e5dfjsn9841522a43b3",
        "X-RapidAPI-Host": "wot-web-risk-and-safe-browsing.p.rapidapi.com"
    }
    #results dictionary to pass to printall
    results = {}

    response = requests.request("GET", url, headers=headers, params=querystring)

    # Convert the response to a list of dictionaries
    data = response.json()

    # Extract the information from the first dictionary in the list
    info = data[0]

    # Extract the web risk rating and create table
    safety = info["safety"]
    rating = safety["status"]
    rating_color = ""
    if rating == "SAFE":
        rating_color = "\033[92m"  # green
    elif rating == "NOT_SAFE":
        rating_color = "\033[91m"  # red 
    elif rating == "SUSPICIOUS":
        rating_color = "\033[93m"  # yellow
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
    #get the url and rating and put into results
    url_name = querystring['t']
    results[url_name]=rating

    # Extract the categories and add them to table
    categories = info["categories"]
    for category in categories:
        name = category["name"]
        confidence = category["confidence"]
        table.add_row([name, confidence])
        #get the category names and confidence and add to results dictioanry
        results[name] = confidence

    print(table)
    #return the results
    return results
