#!/usr/bin/node

const argv = process.argv.slice(2);
const occurrences = parseInt(argv[0]);

if (!occurrences) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < occurrences) {
    console.log('C is fun');
    i++;
  }
}
