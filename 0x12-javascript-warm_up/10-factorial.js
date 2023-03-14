#!/usr/bin/node

const argv = process.argv.slice(2);
const num = parseInt(argv[0]);

function factorial (n) {
  if (!n || n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

console.log(factorial(num));
