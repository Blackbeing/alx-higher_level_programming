#!/usr/bin/node
// Fetch url and print status code
 
// Import request module
const request = require('request');
// Get url
const url = process.argv[2];
 
// Get url
request(url, (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
