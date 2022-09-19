#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  list.forEach(elem => {
    newList.unshift(elem);
  });
  return newList;
};
