#!/usr/bin/node

const argv = process.argv.slice(2);
const size = parseInt(argv[0]);

if (!size) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
