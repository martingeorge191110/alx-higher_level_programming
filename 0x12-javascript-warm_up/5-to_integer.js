#!/usr/bin/node

const prc = process.argv;

if (!prc[2] || isNaN(Number(prc[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.floor(Number(prc[2]))}`);
}
