#!/usr/bin/node

const str = 'X';
const prc = process.argv;

const func = (repStr, argv) => {
  if (!argv[2] || isNaN(Number(argv[2]))) {
    console.log('Missing size');
  }
  for (let i = 0; i < Number(argv[2]); i++) {
    console.log(repStr.repeat(Number(argv[2])));
  }
};

func(str, prc);
