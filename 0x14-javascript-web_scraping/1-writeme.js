#!/usr/bin/node
// Write contents to a file
//
// import fs
const fs = require('fs');
// Get file path first argument in cli
const filepath = process.argv[2];
// Get content to write to file
const content = process.argv[3];
 
// Read file contentes
fs.writeFile(filepath, content, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
