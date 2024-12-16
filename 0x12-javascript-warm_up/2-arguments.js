#!/usr/bin/node

const prc = process.argv

if (prc.length === 2)
   console.log("No argument")
else if (prc.length === 3)
   console.log("Argument found")
else
   console.log("Arguments found")
