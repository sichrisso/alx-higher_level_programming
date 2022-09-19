#!/usr/bin/node
/**
 * defining a class Square that inherits from Square of
 * 5-square.js
 */

const oldSquare = require('./5-square');

class Square extends oldSquare {
  charPrint (c) {
    let k = c;
    if (!c) {
      k = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      console.log(k.repeat(this.width));
    }
  }
}

module.exports = Square;
