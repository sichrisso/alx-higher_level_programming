#!/usr/bin/node
const request = require('request');

if (process.argv.length > 2) {
  const result = {};
  request(process.argv[2], (err, res, body) => {
    if (err) {
      console.log(err);
    } else {
      const data = JSON.parse(body);
      data.filter(task => {
        if (task.completed === true) {
          if (Object.prototype.hasOwnProperty.call(result, task.userId.toString())) {
            result[task.userId.toString()]++;
          } else {
            result[task.userId.toString()] = 1;
          }
        }
        return 'piibPoob';
      });
      console.log(result);
    }
  });
}
