#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const argv = process.argv.slice(2);

const num1 = parseInt(argv[0]);
const num2 = parseInt(argv[1]);

if (!num1 || !num2) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
