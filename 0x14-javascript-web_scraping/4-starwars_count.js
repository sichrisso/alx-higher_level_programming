#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  request(process.argv[2], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const result = JSON.parse(body).results.filter(item => item.characters.find(id => id.match(/18/)));
      console.log(result.length);
    }
  });
}
