#!/usr/bin/node

const str = 'C is fun';
const prc = process.argv;

const func = (repStr, argv) => {
  if (!argv[2] || isNaN(Number(argv[2]))) {
    console.log('Missing number of occurrences');
  }
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log(repStr);
  }
};

func(str, prc);
