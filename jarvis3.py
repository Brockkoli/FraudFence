import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
import requests
import re
import whois
import datetime
import socket

# Load dataset
df = pd.read_csv("phish_dataset.csv")

# Drop Url column
df.drop('Url', axis=1, inplace=True)

# Preprocess data
X = df.drop(['Label'], axis=1)
y = df['Label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Evaluate model on test set
y_pred = clf.predict(X_test)
# print("Accuracy: ", accuracy_score(y_test, y_pred))
# print("Confusion Matrix: ")
# print(confusion_matrix(y_test, y_pred))

# Get user input
url = input("Enter URL: ")
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

try:
    response = requests.get(url)
except:
    pass

# # Preprocess input
# url_data = pd.DataFrame(columns=X.columns)

pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
ip_address = re.match(pattern, url)
if ip_address is not None:
     having_IP_Address = 1
else:
     having_IP_Address = -1

URL_Length = 1 if len(url) > 50 else -1

Shortining_Service = np.where(pd.Series(url).str.contains("bit.ly|tinyurl.com|goo.gl|t.co|ow.ly").any(), 1, -1)
Prefix_Suffix = np.where(pd.Series(url).str.contains("-|.").any(), 1, -1)
having_Sub_Domain = np.where(len(pd.Series(url).str.split('.').tolist()) - 1 > 3, 1, -1)
URL_Depth = url.count("/") - 2
if response is not None and "X-Frame-Options" in response.headers:
    SFH = 1
else:
    SFH = -1

# Query the WHOIS database
domain_info = whois.whois(domain)
# Extract the creation date of the domain
creation_date = domain_info.creation_date
try:
    if type(creation_date) == list:
        creation_date = creation_date[0]
    # Calculate the age of the domain in days
    age_days = (datetime.datetime.now() - creation_date).days
    if age_days < 365:
        age_of_domain = 1
    elif age_days == 0 or age_days > 365:
        age_of_domain = -1
# TypeError: unsupported operand type(s) for -: 'datetime.datetime' and 'NoneType'
except:
     age_of_domain = -1

try:
    socket.gethostbyname(url)
    DNSRecord = 1
except socket.gaierror:
    DNSRecord = -1

if response is not None and response.status_code >= 200 and response.status_code < 400:
    web_traffic = 1
else:
    web_traffic = -1

url_data = pd.DataFrame({
    'having_IP_Address': [having_IP_Address],
    'URL_Length': [URL_Length],
    'Shortining_Service': [Shortining_Service],
    'Prefix_Suffix': [Prefix_Suffix],
    'having_Sub_Domain': [having_Sub_Domain],
    'URL_Depth': [URL_Depth],
    'SFH': [SFH],
    'age_of_domain': [age_of_domain],
    'DNSRecord': [DNSRecord],
    'web_traffic': [web_traffic],
})

# Predict label
prediction = clf.predict(url_data)
if prediction[0] == 1:
    print("The website is suspicious.")
else:
    print("The website is legitimate.")

print(url_data)

plt.figure(figsize=(20,20))
tree = clf.estimators_[0]
plot_tree(tree, feature_names=X.columns, class_names=['legitimate', 'suspicious'], filled=True)
plt.savefig("phishing_tree.png", dpi=600)
