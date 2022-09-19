#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  for (let i = 0; i < x; i++) {
    func();
  }
};
