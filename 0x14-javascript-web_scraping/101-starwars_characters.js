#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
  request(url, (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const movie = JSON.parse(body);
      const namespromises = movie.characters.map(char =>
        new Promise((resolve, reject) => {
          request(char, (err, res, body) => {
            if (err) {
              reject(err);
            } else {
              resolve(JSON.parse(body).name);
            }
          });
        })
      );
      Promise.all(namespromises).then(names => console.log(names.join('\n')));
    }
  });
}
