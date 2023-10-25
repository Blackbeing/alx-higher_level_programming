#!/usr/bin/node
// Write contents to a file
//
// import fs
const fs = require('fs');
const request = require('request');
 
// Get url  as first argument in cli
const url = process.argv[2]
// Get file path second argument in cli
const filepath = process.argv[3]
 
request(url, (err, res, body) => {
  if (err) {
      console.log(err);
  }
  fs.writeFile(filepath, body, 'utf8',  (err) => {
    if (err) {
      console.log(err);
    }
  })
}
);
