#!/usr/bin/node
// Fetch data from API and parse
// Filter only moview by Wedger Antilles, character ID 18
 
const request = require('request');
const starwars = process.argv[2];
 
request(starwars, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    // Return a new array that satisfies conditions -> filter()
    const wedgermovies = data.results.filter((movie) => {
      // check if at least one element in the array satisfies the condition -> some()
      return movie.characters.some((character) => {
        return character.includes(18);
      });
    });
    console.log(wedgermovies.length);
  }
});
 
