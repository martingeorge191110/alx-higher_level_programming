#!/usr/bin/node
const fs = require('fs');
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFileSync(process.argv[3], body, 'utf-8');
  }
});
