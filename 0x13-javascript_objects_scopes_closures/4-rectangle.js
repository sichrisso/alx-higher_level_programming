#!/usr/bin/node
/**
 * defining a Rectangle class with the attributes
 * width and hieght If w or h is equal to 0 or
 * not a positive integer, it create an empty object
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

  rotate () {
    const h = this.height;
    this.height = this.width;
    this.width = h;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
