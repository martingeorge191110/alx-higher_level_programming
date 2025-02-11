#!/usr/bin/node
const request = require('request');

const usersTasks = {};

request(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);

    for (const ele of tasks) {
      if (ele.completed === true) {
        if (!usersTasks[ele.userId]) {
          usersTasks[ele.userId] = 0;
        }
        usersTasks[ele.userId] += 1;
      }
    }
    console.log(usersTasks);
  }
});
