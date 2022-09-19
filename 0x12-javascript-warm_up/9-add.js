#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

function add (a, b) {
  if (a && b) {
    return (a + b);
  }
  return NaN;
}
console.log(add(firstArg, secondArg));
