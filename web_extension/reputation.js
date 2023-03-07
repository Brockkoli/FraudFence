// 192.254.232.148
// http://fasthack.xyz/

const fetch = require('node-fetch');
const dns = require('dns');
const readline = require('readline');

const options = {
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': '81c0482df8msh514a1a1beae15f7p1637ccjsnfcaa82735744',
		'X-RapidAPI-Host': 'ip-reputation-geoip-and-detect-vpn.p.rapidapi.com'
	}
};

// create a readline interface for prompting user input
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question('Enter a URL: ', (url) => {
    url = url.replace(/\/$/, ""); // Remove the trailing forward slash
    console.log(`URL: ${url}`);

    // Perform a DNS lookup to get the IP address
    dns.lookup(url, (err, address, family) => {
        if (err) {
            console.error(err);
            rl.close();
            return;
        }

        console.log(`IP address: ${address}`);

        // Send the GET request to the API using the IP address as the parameter
        fetch(`https://ip-reputation-geoip-and-detect-vpn.p.rapidapi.com/?ip=${address}`, options)
            .then(response => response.json())
            .then(response => console.log(response))
            .catch(err => console.error(err))
            .finally(() => {
                rl.close();
            });
    });
});
