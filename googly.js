const fetch = require('node-fetch');

// Google Safe Browsing API key
const API_KEY = "AIzaSyCHxpPr1VQSqpxwgnG3im7_blJxFy-y8Tg";

// The URL to check
// const url = "http://protintlab.com/";  // unsafe url
// const url = "http://flirteas.za.com/"; // unsafe url
const url = "http://flirteas.za.com/";

// Google Safe Browsing API endpoint
const endpoint = `https://safebrowsing.googleapis.com/v4/threatMatches:find?key=${API_KEY}`;

// Payload data for the API request
const requestData = {
  client: {
    clientId: "your-app-name",
    clientVersion: "1.0.0",
  },
  threatInfo: {
    threatTypes: ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
    platformTypes: ["ANY_PLATFORM"],
    threatEntryTypes: ["URL"],
    threatEntries: [
      {
        url: url,
      },
    ],
  },
};

// Send the API request to check the URL
fetch(endpoint, {
  method: "POST",
  body: JSON.stringify(requestData),
})
  .then((response) => response.json())
  .then((data) => {
    // Check if the URL is safe
    if (data.matches) {
      console.log(`${url} is not safe`);
      console.log(data);
    } else {
      console.log(`${url} is safe`);
      console.log(data);
    }
  })
  .catch((error) => {
    console.error("Error checking URL:", error);
  });
