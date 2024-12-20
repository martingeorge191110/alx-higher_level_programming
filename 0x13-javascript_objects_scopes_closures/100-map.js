#!/usr/bin/node
const list = require('./100-data.js').list;
const mapList = list.map((x, index) => {
  return (x * index);
});

console.log(list);
console.log(mapList);
