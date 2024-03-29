
#  FraudFence

![fraudfence](https://user-images.githubusercontent.com/59412437/226162896-4019fb74-49c0-446f-8659-7812de5510ee.png)


FraudFence, a machine learning tool designed to detect phishing websites by analysing their features. FraudFence includes various website reconnaissance features, such as Whois lookup, port scanning, DNS lookup, server location checking, web header checking, SSL information, trace route, directory busting, and web risk rating. The tool uses a random forest classifier to analyse website features and determine their legitimacy. 
> **Note:** This is an assignment project for  **ICT 2206 Web Security** 

> Singapore Institute of Technology Bachelor of Engineering with Honours in Information and Communications Technology majoring in Information Security
##  Installation

FraudFence can be installed locally by following these steps:
1.  Clone the repository to your local machine.
``` git clone https://github.com/Brockkoli/FraudFence.git```
2.   Install the required dependencies listed in `requirements.txt`.

   ``` cd FraudFence```

   ```pip install -r requirements.txt```

3.  Run `python mainMenu.py` to start the application.

## Features

-   Whois
- register for an API key here: https://rapidapi.com/whoisapi/api/whois-v2/
-   Port scan
	- default: top 1000 most common ports
	- all: 65535 ports
	- custom range: 1-80 for eg
-   DNS lookup
-   Server location checker
-   Web header checker
-   SSL information
-   Trace route
-   Directory busting
	- can use own wordlists
-   Web risk rating
	- register for an API key here: https://rapidapi.com/mywot-mywot-default/api/wot-web-risk-and-safe-browsing
-   Print report
	- generate as report.html

  	![report](https://user-images.githubusercontent.com/59412437/226161527-238ee2f6-b5c7-444b-a6cc-b66109982824.gif)
-   Machine learning URL analyser

### Proof of Concepts
- Graphical User Interface

	![guigif](https://user-images.githubusercontent.com/59412437/226161565-2c7ce0cc-8769-4622-a45d-ad5a1c2937c1.gif)
- Chrome extension

	![guigif](https://user-images.githubusercontent.com/59412437/226160943-bdf7c693-aee9-4733-ac52-5b12f50eaf6d.gif)
  - Google safe browsing
    - register for an API key here: https://developers.google.com/safe-browsing/v4
  - Web of Trust (WOT) database
    - register for an API key here: https://rapidapi.com/mywot-mywot-default/api/wot-web-risk-and-safe-browsing


##  Usage

To use FraudFence, simply enter the URL of the website you want to analyse in the input field and press enter. The tool will perform the analysis, and display the result on the screen.


## Demonstration

[![fraudfence demo](https://user-images.githubusercontent.com/59412437/226162859-91213ea5-689b-4193-93d9-eb07b06f5168.png)](https://youtu.be/0g-ZL4VgCrQ)

