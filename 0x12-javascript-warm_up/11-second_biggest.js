#!/usr/bin/node

const secBig = (argv) => {
  if (!argv[2] || argv.length < 4) {
    console.log(0);
  } else {
    const arr = [];
    for (let i = 2; i < argv.length; i++) {
      arr.push(argv[i]);
    }

    arr.sort((x, y) => x - y);
    console.log(arr[arr.length - 2]);
  }
};

secBig(process.argv);
