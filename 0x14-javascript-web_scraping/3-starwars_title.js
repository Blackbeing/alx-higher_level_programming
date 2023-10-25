#!/usr/bin/node
// Starwars API episode title
 
const request = require('request');
// Concat string
const starwars = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
 
request(starwars, (err, _res, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
