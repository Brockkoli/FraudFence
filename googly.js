//const fetch = require('node-fetch');

// Google Safe Browsing API key
const API_KEY = "AIzaSyCHxpPr1VQSqpxwgnG3im7_blJxFy-y8Tg";

// The URL to check
// const url = "http://protintlab.com/";  // unsafe url
// const url = "http://flirteas.za.com/"; // unsafe url
const url1 = "http://flirteas.za.com/";

async function fetchData() {
    // Google Safe Browsing API endpoint
    const endpoint = `https://safebrowsing.googleapis.com/v4/threatMatches:find?key=${API_KEY}`;

    // Payload data for the API request
    const requestData = {
    client: {
        clientId: "fraudfence",
        clientVersion: "1.0.0",
    },
    threatInfo: {
        threatTypes: ["MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE", "POTENTIALLY_HARMFUL_APPLICATION"],
        platformTypes: ["ANY_PLATFORM"],
        threatEntryTypes: ["URL"],
        threatEntries: [
                {
                    url: url1,
                },
            ],
        },
    };

    try {
        // Send the API request to check the URL
        const res = await fetch(endpoint, {
            method: "POST",
            body: JSON.stringify(requestData),
        });
        //.then((response) => response.json())
        const data = await res.json()

        // Check if the URL is safe
        if (data.matches) {
            //console.log(`${url} is not safe`);
            const googlydb = data;
            const threat = data.matches[0].threat;
            // console.log('threat: ', threat);

            document.getElementById('googly').innerHTML = `
                <p class="safety safety--unsafe">${url1} is not safe</p>
                <p>Checked against database: ${JSON.stringify(googlydb)}</p>
                <p>Threat: ${JSON.stringify(threat)}</p>
            `;
        } else {
            //console.log(`${url} is safe`);
            const googlydb = data;
            const threat = data.matches[0].threat;
            document.getElementById('googly').innerHTML = `
                <p class="safety safety--safe">${url1} is safe</p>
                <p>Checked against database: ${JSON.stringify(googlydb)}</p>
                <p>Threat: ${JSON.stringify(threat)}</p>
            `;
        }
    } catch(error) {
        console.error("Error checking URL:", error);
    };
}

fetchData();