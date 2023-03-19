//WOT Web Risk and Safe browsing

// Get the current tab
chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
  // Get the URL of the current tab
  let url = tabs[0].url;
  url = url.replace(/\/$/, ""); // Remove the trailing forward slash
  console.log(url); 



async function fetchData(url) {
  const options = {
    method: 'GET',
    headers: {
      'X-RapidAPI-Key': '1451a54239msh9a771e3bcb0b237p16e5dfjsn9841522a43b3',
      'X-RapidAPI-Host': 'wot-web-risk-and-safe-browsing.p.rapidapi.com'
    }
  };

  const res = await fetch(`https://wot-web-risk-and-safe-browsing.p.rapidapi.com/targets?t=${url}`, options)
  const record = await res.json()
    .then((data) => {
      // extract the necessary data from the JSON object
      // if (data && data[0]) {
      if (data[0]) {
          const target = data[0].target;
          const safety = data[0].safety;
          const status = data[0].safety.status;
          const reputation = data[0].safety.reputations;
          const confidence = data[0].safety.confidence;

          const childSafety = data[0].childSafety;
          const csreputation = data[0].childSafety.reputations;
          const csconfidence = data[0].childSafety.confidence;
          const categories = data[0].categories.map(category => category.name).join(', ');
          // const categories = data[0].categories;


        // Update reputation progress bar
        const reputationBar = document.getElementById('reputation-bar');

        // Update score in span beside progress bar
        const reputationScore = document.getElementById('reputation-score');

        reputationBar.value = reputation; // set the progress bar value
        reputationScore.textContent = reputation; // set the score next to the progress bar

        // convert data to json string and display in the HTML page
        document.getElementById('webrisk').innerHTML = `
          <p>Target: ${target}</p>
          <h4>Safety: </h4>
          <p>Status: ${JSON.stringify(status).replace(/[""]/g, '')}</p>
          <p>Reputation: ${JSON.stringify(reputation)}</p>
          <p>Confidence: ${JSON.stringify(confidence)}</p>
          <h4>Child Safety: </h4>
          <p>Reputation: ${JSON.stringify(csreputation)}</p>
          <p>Confidence: ${JSON.stringify(csconfidence)}</p>
          <h4>WOT Category: </h4>
          <p>Category: ${JSON.stringify(categories).replace(/[""]/g, '')}</p>
          `; 
      } else {
        document.getElementById('webrisk').innerHTML = `
          <p>No data found for ${url}.</p>
          `;
      }
      
    })
    .catch((err) => console.error(err));
  }

  fetchData(url);

});
