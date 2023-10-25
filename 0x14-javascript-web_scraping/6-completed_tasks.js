#!/usr/bin/node
// Accumulate data from API
 
const request = require('request');
const url = process.argv[2];
 
request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);

  const usercount = data.reduce((accumulator, data) => {
    if (data.completed) {
      accumulator[data.userId] = (accumulator[data.userId] || 0) + 1;
    }
    return accumulator;
  }, {});
    // // in python code
    // usercount = {}
    // for data in data:
    //     if data['completed']:
    //         usercount[data['userId']] = usercount.get(data['userId'], 0) + 1
  console.log(usercount);
});
