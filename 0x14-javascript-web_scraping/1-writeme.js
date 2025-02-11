#!/usr/bin/node
const fs = require('fs');

const writingFiles = async (path, content) => {
  try {
    fs.writeFileSync(path, content);
  } catch (err) {
    console.log(err);
  }
};

writingFiles(process.argv[2], process.argv[3]);
