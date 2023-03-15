//WOT Web Risk and Safe browsing

//const readline = require('readline').createInterface({
  //input: process.stdin,
 // output: process.stdout
//});

//readline.question('Enter your input: ', (input) => {
  //console.log(`You entered: ${input}`);
  //readline.close();
//});
// const fetch = require('node-fetch');

// const url = "http://flirteas.za.com/"
// const url = "http://www.y8.com"


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
      'X-RapidAPI-Key': '3050331b8fmsh63e50212984ee13p1b8a2djsn12d21cb50bc0',
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
      /*
      // iterate elements of objects and display individually
      document.getElementById('json-data').innerHTML = `
      <p>Target: ${target}</p>
      <p>Safety: ${
        Object.entries(safety)
          .map(([key, value]) => `${key}: ${value}`)
          .join('<br>')
      }</p>
      <p>Child Safety: ${
        Object.entries(childSafety)
          .map(([key, value]) => `${key}: ${value}`)
          .join('<br>')
      }</p>
      <p>Categories: ${
        categories
          .map(category => category.name)
          .join(', ')
      }</p>
    `;
    */

    /*
    // for testing
    console.log(target)
    console.log(safety)
    console.log(childSafety)
    console.log(categories) */
      
    })
    .catch((err) => console.error(err));
  }

  fetchData(url);

});