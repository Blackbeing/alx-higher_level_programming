#!/usr/bin/node

const SquareBase = require('./5-square.js');

class Square extends SquareBase {
  charPrint (c) {
    const myChar = c || 'X';
    for (let i = 0; i < this.height; i++) {
      let mystring = '';
      for (let j = 0; j < this.width; j++) {
        mystring += myChar;
      }
      console.log(mystring);
    }
  }
}
module.exports = Square;
