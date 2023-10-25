#!/usr/bin/node
// Read contents of a file
 
// import fs
const fs = require('fs');
// Get file path first argument in cli
const filepath = process.argv[2];
 
// Read file contentes
fs.readFile(filepath, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
 

