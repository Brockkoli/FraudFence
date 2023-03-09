import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import requests

# Load the dataset
data = pd.read_csv('phishing_url_dataset.csv')

# Split the data into features (X) and target (y)
X = data.drop('target', axis=1)
y = data['target']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Ask the user for a URL to classify
url = input("Enter a URL to classify: ")

try:
    response = requests.get(url)
except:
    pass

# Extract the features from the URL
url_length = len(url)
if response.status_code >= 200 and response.status_code < 400:
    valid_url = 1
else:
    valid_url = 0
at_symbol = 1 if '@' in url else 0
sensitive_words_count = sum(1 for word in ['password', 'bank', 'login', 'security', 'authkey'] if word in url)
path_length = len(url.split('/')[-1])
isHttps = 1 if 'https' in url else 0
nb_dots = url.count('.')
nb_hyphens = url.count('-')
nb_and = url.count('&')
nb_or = url.count('|')
nb_www = 1 if 'www' in url else 0
nb_com = 1 if 'com' in url else 0
nb_underscore = url.count('_')

# Create a DataFrame with the extracted features
new_data = pd.DataFrame({
    'url_length': [url_length],
    'valid_url': [valid_url],
    'at_symbol': [at_symbol],
    'sensitive_words_count': [sensitive_words_count],
    'path_length': [path_length],
    'isHttps': [isHttps],
    'nb_dots': [nb_dots],
    'nb_hyphens': [nb_hyphens],
    'nb_and': [nb_and],
    'nb_or': [nb_or],
    'nb_www': [nb_www],
    'nb_com': [nb_com],
    'nb_underscore': [nb_underscore],
})

# Use the trained model to predict whether the URL is phishing or legitimate
prediction = clf.predict(new_data)

# Print the result
if prediction[0] == 1:
    print("The URL seems legitimate.")
    print(new_data)
else:
    print("The URL seems suspicious.")
