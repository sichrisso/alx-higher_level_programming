#!/usr/bin/node
/**
 * defining the class Square that inherits from the
 * Rectangle class
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
