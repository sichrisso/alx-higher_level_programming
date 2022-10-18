#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
  request(url, (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const movie = JSON.parse(body);
      movie.characters.map(char => {
        request(char, (err, res, body) => {
          if (err) {
            console.log(err);
          } else {
            console.log(JSON.parse(body).name);
          }
        });
        return (char);
      });
    }
  });
}
