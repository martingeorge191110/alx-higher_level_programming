#!/usr/bin/node

exports.esrever = function (list) {
  let i = list.length - 1;
  const arr = [];

  while (i >= 0) {
    arr.push(list[i]);
    i--;
  }

  return (arr);
};
