#!/usr/bin/node

const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint(c) {
    // If c is undefined, use the character 'X'
    const character = c || 'X';

    // Print the square using the specified character
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }
}

module.exports = Square;
