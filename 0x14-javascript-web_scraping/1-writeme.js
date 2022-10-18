#!/usr/bin/node
const fs = require('fs');

if (process.argv.length > 3) {
  fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
    if (err) console.log(err);
  });
}
