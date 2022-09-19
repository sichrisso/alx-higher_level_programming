#!/usr/bin/node
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
const fs = require('fs');

let text = '';
if (fileA !== undefined && fileB !== undefined &&
    fileC !== undefined) {
  if ((fs.existsSync(fileA) && fs.statSync(fileA).isFile) &&
    (fs.existsSync(fileB) && fs.statSync(fileB).isFile)) {
    text += fs.readFileSync(fileA, (error) => {
      if (error) throw error;
    });

    text += fs.readFileSync(fileB, (error) => {
      if (error) throw error;
    });

    fs.writeFile(fileC, text, (error) => {
      if (error) throw error;
    });
  }
}
