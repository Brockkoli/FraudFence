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
const url = "http://www.y8.com"

async function fetchData() {
  const options = {
    method: 'GET',
    headers: {
      'X-RapidAPI-Key': '39a04747b6msh4609958369c99c5p11cea8jsna440a75be8bc',
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
          const childSafety = data[0].childSafety;
          //const categories = data[0].categories.map(category => category.name).join(', ');
          const categories = data[0].categories;

        // convert data to json string and display in the HTML page
        document.getElementById('webrisk').innerHTML = `
          <p>Target: ${target}</p>
          <p>Safety: ${JSON.stringify(safety)}</p>
          <p>Child Safety: ${JSON.stringify(childSafety)}</p>
          <p>Categories: ${JSON.stringify(categories)}</p>
          `; 
      } else {
        document.getElementById('webrisk').innerHTML = `
          <p>No data found.</p>
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

  fetchData();