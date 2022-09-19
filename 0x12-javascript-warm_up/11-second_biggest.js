#!/usr/bin/node
const args = process.argv;
let bigest = 0;
let secBig = 0;
let num;
if (process.argv.length < 4) {
  console.log('0');
} else {
  for (let i = 2; i < args.length; i++) {
    num = parseInt(args[i]);
    if (num > bigest) {
      secBig = bigest;
      bigest = num;
    } else if (num > secBig) {
      secBig = num;
    }
  }
  console.log(secBig);
}
