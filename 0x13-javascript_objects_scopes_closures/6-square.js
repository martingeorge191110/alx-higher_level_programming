#!/usr/bin/node
const ParentSquare = require('./5-square');

module.exports = class Square extends ParentSquare {
  charPrint = (c) => {
    if (!c) {
      return (this.charPrint('X'));
    }

    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.width));
    }
  };
};
