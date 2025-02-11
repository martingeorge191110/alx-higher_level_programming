#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
let movieLength = 0;

request.get(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    for (const ele of results) {
      for (const e of ele.characters) {
        if (e.search('18') > 0) {
          movieLength += 1;
        }
      }
    }
  }
  console.log(movieLength);
});
