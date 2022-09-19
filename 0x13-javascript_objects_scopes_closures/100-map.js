#!/usr/bin/node
const arr = require('./100-data');
const newList = arr.list.map((elem, idx) => elem * idx);
console.log(arr.list);
console.log(newList);
