//WOT Web Risk and Safe browsing

const fetch = require('node-fetch'); // Import the node-fetch library
const url = "https://www.google.com"

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '81c0482df8msh514a1a1beae15f7p1637ccjsnfcaa82735744',
		'X-RapidAPI-Host': 'wot-web-risk-and-safe-browsing.p.rapidapi.com'
	}
};

fetch(`https://wot-web-risk-and-safe-browsing.p.rapidapi.com/targets?t=${url}`, options)
    .then(response => response.json())
    .then(response => console.log(response))
    .catch(err => console.error(err))