#!/usr/bin/node

const prc = process.argv;

if (prc[2]) {
  console.log(prc[2]);
} else {
  console.log('No argument');
}
