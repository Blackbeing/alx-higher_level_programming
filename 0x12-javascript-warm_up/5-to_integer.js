#!/usr/bin/node

const argv = process.argv.slice(2);
const myNumber = parseInt(argv[0]);

if (!myNumber) {
  console.log('Not a number');
} else {
  console.log(`My number: ${myNumber}`);
}
