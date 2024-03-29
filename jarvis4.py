import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, roc_curve
from sklearn.model_selection import train_test_split, learning_curve
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import seaborn as sns
import xgboost as xgb
from xgboost import plot_importance

import requests
import re
import whois
import datetime
import socket
import ssl
import whois
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import colorama

def jarvis4(url):
    colorama.init()
    print("\nRunning Jarvis[*]")
    # Load the dataset
    data = pd.read_csv('phish4.csv')

    # Drop Url column
    data.drop('index', axis=1, inplace=True)

    # Preprocess data
    X = data.drop(['Result'], axis=1)
    y = data['Result']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    # Evaluate model on test set
    y_pred = clf.predict(X_test)
    print(colorama.Fore.GREEN + "\nAccuracy: ", accuracy_score(y_test, y_pred))

    '''
    [[true_negatives false_positives]
    [false_negatives true_positives]]
    '''
    print(colorama.Fore.RED + "\nConfusion Matrix: ")
    cm = confusion_matrix(y_test, y_pred)
    # print(confusion_matrix(y_test, y_pred))
    print(cm)
    print("\n" + colorama.Style.RESET_ALL)

    # assuming y_true and y_pred are your true labels and predicted labels, respectively
    fpr, tpr, thresholds = roc_curve(y_test, y_pred)

    # plot ROC curve
    roc = plt
    roc.figure()
    roc.plot(fpr, tpr)
    roc.xlabel('False Positive Rate')
    roc.ylabel('True Positive Rate')
    roc.title('ROC Curve')
    roc.savefig('roc.png')
    print("Plotting ROC curve.")

    # plot the confusion matrix
    cmat = plt
    cmat.figure()
    sns.heatmap(cm, annot=True, cmap="Blues", fmt="d")
    cmat.title("Confusion Matrix")
    cmat.xlabel("Predicted Class")
    cmat.ylabel("True Class")
    # save the plot as an image file
    cmat.savefig('confusion_matrix.png')
    print("Plotting the Confusion Matrix.")

    # Plot feature importances
    feature = plt
    feature.figure(figsize=(28, 21))
    importances = clf.feature_importances_
    feature_names = X.columns
    feature.barh(feature_names, importances)
    feature.xlabel("Feature importance")
    feature.ylabel("Feature name")
    feature.title("Random Forest Classifier Feature Importances")
    feature.savefig('feature.png')
    print("Plotting the Random Forest Classifier Feature Importances.\n")

    # Plot the learning curves
    # Calculate learning curve scores
    train_sizes, train_scores, test_scores = learning_curve(
        clf, X_train, y_train, cv=5, scoring='accuracy', n_jobs=-1)

    # Plot learning curves
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.figure()
    plt.title("Learning Curve")
    plt.xlabel("Training Examples")
    plt.ylabel("Score")
    plt.ylim(0.0, 1.1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    
    plt.title("Learning Curve")
    plt.savefig('learning_curve.png')
    learning_curve_plot = plt
    print("Plotting the Learning Curve.\n")
    # learning_curve_plot.show()

    # Get user input
    domain = url
    if domain.startswith("https://"):
        domain = domain.strip("https://")
    elif domain.startswith("http://"):
        domain = domain.strip("http://")
    elif domain.startswith("www"):
        domain = domain.strip("www")
    elif domain.startswith("https://www"):
        domain = domain.strip("https://www")
    elif domain.startswith("http://www"):
        domain = domain.strip("http://www")

    response = None

    # list of suspicious features/characteristics
    sus_things = []

    # list of legitimate features/characteristics
    legit_things = []

    try:
        response = requests.get(url)
    except:
        pass

    # # Preprocess input
    # url_data = pd.DataFrame(columns=X.columns)

    '''
    -1: Phishing
    0: Suspicious
    1: Legitimate
    http://stolizaparketa.ru/wp-content/themes/twentyfifteen/css/read/chinavali/index.php?email=_xxx@yyy.com____
    https://s.id/log-lBPER
    '''

    '''
    To check URL for IP address (even in hexadecimal)
    Example:
    http://125.31.12.321/scam.com will return -1
    https://0x7f000001/index.html will return -1
    https://www.youtube.com/index.html will return 1
    '''

    try:
        print("Scanning for any IP address in URL...")
        # regular expression to match an IP address
        ip_regex = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

        # regular expression to match a hexadecimal IP address
        hex_ip_regex = r'^0x[0-9a-fA-F]{8}$'

        # extract the domain from the URL
        domainUrl = re.findall(r'(?<=://)[\w.-]+(?<=/)?', url)

        # check if the domain is an IP address or a hexadecimal IP address
        if re.match(ip_regex, domainUrl[0]) or re.match(hex_ip_regex, domainUrl[0]):
            having_IP_Address = -1
            sus_things.append('IP address detected in url.')
        else:
            having_IP_Address = 1
            legit_things.append('IP address not detected in url.')
        print("Scanning for any IP address in URL completed.")

        '''
        To check the length of URL
        Example:
        URL length > 75 return -1
        54 <= URL length <= 75 will return 0
        URL length < 54 will return 1
        '''
        print("Looking at length of URL...")
        if len(url) > 75:
            URL_Length = -1
            sus_things.append(f'Extremely long url of length {len(url)} detected in url.')
        elif 54 <= len(url) <= 75:
            URL_Length = 0
            sus_things.append(f'Long url of length {len(url)} detected in url.')
        else:
            URL_Length = 1
            legit_things.append(f'Normal length of {len(url)} detected in url.')
        print("Finished ooking at length of URL.")

        '''
        To check whether URL is shortened
        Example:
        https://bit.ly/3t4Shwb will return -1
        '''
        print("Scanning URL for any shortened service...")
        shortened_domains = ["bit.ly", "goo.gl", "t.co", "tinyurl.com", "ow.ly", "is.gd", "buff.ly", "adf.ly",
                             "twitthis.com", "tweez.me", "v.gd", "qr.net", "1url.com", "link.zip.net", "url4.eu",
                             "cli.gs", "qr.ae", "fic.kr", "su.pr", "loopt.us", "scrnch.me", "vzturl.com", "tiny.cc",
                             "tr.im", "prettylinkpro.com", "cutt.us", "ping.fm", "snipr.com", "snipurl.com",
                             "post.ly", "mcaf.ee", "q.gs", "db.tt", "filoops.info", "wp.me", "twurl.nl", "j.mp",
                             "x.co", "cur.lv", "rubyurl.com", "kl.am", "yourls.org", "doiop.com", "buzurl.com",
                             "fb.me", "bkite.com", "yfrog.com", "bit.do", "ow.ly", "bitly.com", "lnkd.in",
                             "po.st", "u.to", "go2l.ink", "rebrand.ly", "x.co", "rb.gy", "short.to"]

        shortened_domains_count = 0
        for shortdomain in shortened_domains:
            if re.search(shortdomain, url):
                shortened_domains_count += 1
                break

        if shortened_domains_count > 1:
            Shortining_Service = -1
            sus_things.append('Shortened detected in url.')
        else:
            Shortining_Service = 1
            legit_things.append('Shortening service not used in url.')
        print("Finished scanning URL for any shortened service.")

        '''
        To check whether URL have @ symbol
        Example:
        https://google@gmail.com will return -1
        '''
        print("Scanning for @ symbol in URL.")
        if '@' in url:
            having_At_Symbol = -1
            sus_things.append('@ detected in url.')
        else:
            having_At_Symbol = 1
            legit_things.append('@ not detected in url.')
        print("Finished scanning for @ symbol in URL.")

        '''
        To check for “//” in the URL
        Example:
        https://www.example.com//https://www.fake.com will return -1. 
        The above url might be interpreted as https://www.fake.com by the browser.
        '''
        print("Scanning for // symbol in URL...")
        if url.startswith("https://"):
            base_url = url.replace("https://", "", 1)
        elif url.startswith("http://"):
            base_url = url.replace("http://", "", 1)
        if '//' in base_url:
            double_slash_redirecting = -1
            sus_things.append('Additional // detected in url.')
        else:
            double_slash_redirecting = 1
            legit_things.append('Additional // not detected in url.')
        print("Finished scanning for // symbol in URL.")

        '''
        To check for '-' hyphen in URL
        Example:
        https://shopee-payme.com will return -1
        '''
        print("Scanning for - symbol in URL...")
        Prefix_Suffix = np.where(pd.Series(url).str.contains("-").any(), -1, 1)
        if Prefix_Suffix == -1:
            sus_things.append('Hyphen (-) detected in url.')
        else:
            legit_things.append('Hyphen (-) not detected in url.')
        print("Finished scanning for hyphen (-) symbol in URL.")

        '''
        # To check for number of sub-domains in URL
        # After removing main domain and top level domain, 
        # If 0 <= sub-domain <= 1, return 1
        # If sub-domain == 2, return 0
        # If sub-domain == 3, return -1
        # '''
        print("Counting subdomains in URL...")
        # remove the scheme (http, https) if present
        if url.startswith('http://'):
            url1 = url[7:]
        elif url.startswith('https://'):
            url1 = url[8:]

        # split the remaining URL by dots and count the resulting parts
        parts = url1.split('.')
        num_subdomains = len(parts) - 2  # exclude main domain and TLD

        if 0 <= num_subdomains <= 1:
            having_Sub_Domain = 1
            legit_things.append('Less than 2 sub-domains detected in url.')
        elif num_subdomains == 2:
            having_Sub_Domain = 0
            sus_things.append('2 sub-domains detected in url.')
        else:
            having_Sub_Domain = -1
            sus_things.append('More than 2 sub-domains detected in url.')
        print("Finished counting subdomains in URL...")

        '''
        To check whether certificate authority is well known and trustworthy
        If CA Is trusted and age of certificate >= 365 days, return 1
        If CA is trusted and age of certificate < 365 days, return 0
        If CA is not trusted, return 0
        Else, return -1
        '''
        print("Checking Certificate Authority...")

        def get_ssl_info(url):
            context = ssl.create_default_context()
            try:
                with socket.create_connection((url, 443)) as sock:
                    with context.wrap_socket(sock, server_hostname=url) as ssock:
                        cert = ssock.getpeercert()
                        issuer = dict(x[0] for x in cert['issuer'])
                        validity_end = datetime.datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z')
                        validity_days = (validity_end - datetime.datetime.now()).days
            except:
                print("passing")
                pass

            return issuer.get('organizationName', None), validity_days

        # Example usage:
        issuer, validity_days = get_ssl_info('y8.com')

        trusted_cert_authorities = ['DigiCert', 'GlobalSign', 'Verizon', 'Symantec', 'Entrust', 'Comodo',
                                    'GoDaddy', 'Network Solutions', 'Thawte', 'GeoTrust', 'IdenTrust',
                                    'Google Trust Services LLC', 'Let\'s Encrypt']

        if issuer in trusted_cert_authorities and validity_days >= 365:
            SSLfinal_State = 1
            legit_things.append('Trusted CA with validity of more than a year.')

        elif issuer in trusted_cert_authorities and validity_days < 365:
            SSLfinal_State = 0
            sus_things.append('Trusted CA with validity of less than a year.')

        elif issuer not in trusted_cert_authorities:
            SSLfinal_State = 0
            sus_things.append('CA not trusted.')
        else:
            SSLfinal_State = -1
            sus_things.append('CA not found.')

        '''
        To check domain registration duration of URL
        If domain reg duration > 365 days, return 1
        If domain reg duration is none (whois can't extract info), return 0
        If domain reg duration <= 365 days, return -1
        '''

        def get_domain_registration_duration(url):
            try:
                creation_date = whois.whois(url).creation_date
                if isinstance(creation_date, list):
                    creation_date = creation_date[0]
                expiration_date = whois.whois(url).expiration_date
                if isinstance(expiration_date, list):
                    expiration_date = expiration_date[0]
                duration = expiration_date - creation_date
                return duration.days
            except:
                pass

        try:
            registration_duration = get_domain_registration_duration(url)
            if registration_duration is None:
                registration_duration = 0
            reg_days = int(registration_duration)

            print("Domain registration duration:", reg_days, "days")
            if reg_days > 365:
                Domain_registeration_length = 1
                legit_things.append('Domain registration duration more than a year.')
            elif 0 < reg_days <= 365:
                Domain_registeration_length = -1
                sus_things.append('Domain registration duration less than a year.')
            else:
                Domain_registeration_length = 0
                sus_things.append('Domain registration duration not found.')
        except:
            Domain_registeration_length = 0
            sus_things.append('Domain registration duration not found.')

        '''
        To check favicon of URL
        If favicon is loaded from external domain, return -1
        If favicon is loaded from internal domain, return 1
        Else, return 0
        '''
        # response = requests.get(url)
        try:
            soup = BeautifulSoup(response.text, "html.parser")
            print("Looking at favicon...")
            favicon_url = None
            if soup.find("link", rel="icon"):
                favicon_url = soup.find("link", rel="icon")["href"]
            elif soup.find("link", rel="shortcut icon"):
                favicon_url = soup.find("link", rel="shortcut icon")["href"]

            if favicon_url:
                parsed_url = urlparse(url)
                parsed_favicon_url = urlparse(favicon_url)

                if parsed_url.netloc != parsed_favicon_url.netloc:
                    Favicon = -1
                    sus_things.append('Favicon is loaded from external domain.')
                else:
                    Favicon = 1
                    legit_things.append('Favicon is loaded from internal domain.')
            else:
                Favicon = 0
            print("Favicon analysed.")
        except:
            Favicon = 0
            sus_things.append('Favicon unable to be determined.')

        '''
        To check for uncommon ports opened by the website.
        The following are common ports opened:
        Port 80 (HTTP): This is the default port for serving web pages. It is used for unsecured web traffic.
        Port 443 (HTTPS): This is the default port for serving secure web pages. It is used for encrypted web traffic.
        Port 21 (FTP): This is used for transferring files to and from a server over the internet. It is used by FTP clients to connect to FTP servers.
        Port 22 (SSH): This is used for secure remote login and other secure network services over an unsecured network.
        Port 25 (SMTP): This is used for sending email messages between servers. It is used by email clients to send email messages.
        Port 110 (POP3): This is used for retrieving email messages from a server. It is used by email clients to download email messages.
        Port 143 (IMAP): This is used for retrieving email messages from a server. It is used by email clients to download email messages.
        Scan from port 1 to 500:
        If uncommon_ports_count == 1, return 0
        If uncommon_ports_count > 1, return -1
        Else, return 1
        '''
        # Define the list of common ports used for websites
        website_ports = [80, 443, 21, 22, 25, 110, 143]

        # Get the IP address of the URL
        try:
            ip_address = socket.gethostbyname(url)
            print("Scanning ports for", url, "(", ip_address, ")")

            uncommon_ports_count = 0

            # Scan ports 1-500
            # for port in range(1, 500):
            for port in range(1, 10):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((ip_address, port))
                if result == 0:
                    if port not in website_ports:
                        uncommon_ports_count += 1
                sock.close()

                # Print out progress message
                print("Scanned port", port, end="\r")

            if uncommon_ports_count == 1:
                port = 0
                sus_things.append('1 uncommon ports found opened.')
            elif uncommon_ports_count > 1:
                port = -1
                sus_things.append('More than 1 uncommon ports found opened.')
            else:
                port = 1
                legit_things.append('Common ports found opened.')
        except:
            port = 0
            sus_things.append('Port scanning not executed on IP.')

        print("Finished analysing ports.")

        '''
        To check for 'https' token in URL
        If URL starts with https://, return 1
        If URL starts with http://, return -1
        '''
        print("Checking https token...")
        if url.startswith("https:"):
            HTTPS_token = 1
            legit_things.append('HTTPS in use.')
        else:
            HTTPS_token = -1
            sus_things.append('HTTPS not used.')
        print("Finished checking https token.")

        '''
        To check whether the tags in the webpage are loaded from external domains.
        If < 0.22 of tags loaded from external domains, return 1
        If 0.22 <= tags <= 0.61 loaded from external domains, return 0
        Else, return 1
        '''
        # response = requests.get(url)
        print("Looking at tags...")
        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            external_urls = []
            for tag in soup.find_all():
                if tag.has_attr('src') or tag.has_attr('href'):
                    attr = 'src' if tag.has_attr('src') else 'href'
                    href = tag[attr]
                    if href.startswith('http'):
                        external_urls.append(href)

            parsed_url = urlparse(url)
            total_urls = len(external_urls)
            external_count = 0

            for external_url in external_urls:
                parsed_external_url = urlparse(external_url)
                if parsed_external_url.netloc != parsed_url.netloc:
                    external_count += 1
            try:
                if external_count / total_urls < 0.22:
                    Request_URL = 1
                    legit_things.append('Most tags loaded internally.')
                elif 0.22 <= external_count / total_urls <= 0.61:
                    Request_URL = 0
                    sus_things.append('Significant number of tags loaded from external domains.')
                else:
                    Request_URL = -1
                    sus_things.append('Most tags loaded from external domains.')
            except ZeroDivisionError:
                Request_URL = 0
                sus_things.append('No tags found.')
        except:
            Request_URL = 0
            sus_things.append('Tags not determined')
        print("Finished analysing tags.")

        '''
        To check how many times the website is redirected
        If the number of redirects ≤ 1, return 1
        If the number of redirects ≥ 2 And < 4, return 0
        Else, return -1
        '''
        redirect_count = 0
        print("Looking at number of redirects...")
        while True:
            try:
                response = requests.get(url)
            except:
                break
            if response.history:
                url = response.url
                redirect_count += 1
                print("url:", url)
                print("redirect count:", redirect_count)
            else:
                break

        if redirect_count <= 1:
            Redirect = 1
            sus_things.append('Less than 2 redirects detected.')
        elif 2 <= redirect_count < 4:
            Redirect = 0
            sus_things.append('More than 1 redirect detected.')
        else:
            Redirect = -1
            sus_things.append('More than 3 redirects detected.')
        print("Finished looking at redirects.")

        '''
        To check whether right-click is disabled in the website
        Look for event.button==2 in source code
        If right-click is disabled, return -1
        Else, return 1
        '''
        # response = requests.get(url)
        print("Looking at right-click events...")
        try:
            html = response.text
            if "event.button==2" in html:
                RightClick = -1
                sus_things.append('Right-click might be disabled.')
            else:
                RightClick = 1
                legit_things.append('Right-click not disabled.')
        except:
            RightClick = 0
            sus_things.append('Right-click event not detectable.')
        print("Finished looking at right-click events.")

        '''
        To check whether there is any popup windows in the website
        If there is popups, return -1
        Else, return 1
        '''
        # response = requests.get(url)
        print("Looking at pop up events...")
        try:
            soup = BeautifulSoup(response.content, 'html.parser')

            pop_up_text = []
            for tag in soup.find_all():
                if tag.has_attr('onclick'):
                    onclick = tag['onclick']
                    if 'window.open' in onclick:
                        pop_up_text.append(tag.text)

            if pop_up_text:
                popUpWindow = -1
                sus_things.append('Pop up windows detected.')
            else:
                popUpWindow = 1
                legit_things.append('No pop up windows detected.')
        except:
            popUpWindow = 0
            sus_things.append('Pop up windows unable to be determined.')
        print("Finished looking at popup events.")

        '''
        To check whether the iframe tag frameBorder attribute is used to create an invisible frame
        If iframe is used, return -1
        Else, return 1
        '''
        # response = requests.get(url)
        print("Looking at iframe...")
        try:
            soup = BeautifulSoup(response.content, 'html.parser')

            iframes = soup.find_all('iframe')
            for iframe in iframes:
                if iframe.has_attr('frameborder'):
                    Iframe = -1
                    sus_things.append('iframe tag detected.')
                    break
            else:
                Iframe = 1
                legit_things.append('No iframe tag detected.')
        except:
            Iframe = 0
            sus_things.append('iframe tag unable to be detected.')
        print("Finished looking at iframe.")

        url_data = pd.DataFrame({
            'having_IP_Address': [having_IP_Address],
            'URL_Length': [URL_Length],
            'Shortining_Service': [Shortining_Service],
            'having_At_Symbol': [having_At_Symbol],
            'double_slash_redirecting': [double_slash_redirecting],
            'Prefix_Suffix': [Prefix_Suffix],
            'having_Sub_Domain': [having_Sub_Domain],
            'SSLfinal_State': [SSLfinal_State],
            'Domain_registeration_length': [Domain_registeration_length],
            'Favicon': [Favicon],
            'port': [port],
            'HTTPS_token': [HTTPS_token],
            'Request_URL': [Request_URL],
            'Redirect': [Redirect],
            'RightClick': [RightClick],
            'popUpWindow': [popUpWindow],
            'Iframe': [Iframe],
        })

        # Print out each characteristics detected
        print(colorama.Fore.GREEN + "\nSAFE Characteristics:\n")
        print(colorama.Fore.GREEN + "\n\t".join(legit_things) + colorama.Style.RESET_ALL)
        print(colorama.Fore.RED + "\nSUSPICIOUS Characteristics:\n")
        print(colorama.Fore.RED + "\n\t".join(sus_things) + colorama.Style.RESET_ALL)

        # Predict label
        prediction = clf.predict(url_data)
        if prediction[0] == -1:
            print(f"\nThe website {url} is " + colorama.Fore.RED + "SUSPICIOUS.\n" + colorama.Style.RESET_ALL)
        else:
            print(f"\nThe website {url} is " + colorama.Fore.GREEN + "LEGITIMATE.\n" + colorama.Style.RESET_ALL)


        # Set display options
        pd.set_option('display.max_columns', None)
        pd.set_option('display.max_rows', None)
        print(colorama.Fore.MAGENTA + '*' * 50 + colorama.Style.RESET_ALL)
        # print(url_data)

        # # Plot decision tree
        # plt.figure(figsize=(55, 30))
        # tree = clf.estimators_[0]
        # plot_tree(tree, feature_names=X.columns, class_names=['legitimate', 'suspicious'], filled=True)
        # plt.title("Random Forest Decision Tree")
        # plt.savefig("phishing_tree.png", dpi=600)
        # print("Decision tree image created!")
        # # plt.show()

    except:
        print("\nThe website is suspicious.")

    return(legit_things, sus_things)

