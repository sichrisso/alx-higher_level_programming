#!/usr/bin/node
/*
  defining a Rectangle class with the attributes
  width and height
  If w or h is equal to 0 or not a positive integer
  it create an empty object
*/

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
