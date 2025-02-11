#!/usr/bin/node
const fs = require('fs');


const readingFiles = async (path) => {
   try {
      const content = fs.readFileSync(path, "utf-8")
      console.log(content)
   } catch (err) {
      console.log(err)
   }
}

readingFiles(process.argv[2])
