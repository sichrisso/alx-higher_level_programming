#!/usr/bin/node
exports.addMeMaybe = function (n, func) {
  n++;
  func(n);
};
