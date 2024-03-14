#!/usr/bin/node
exports.esrever = function (list) {
  let newArray = [];
  while (list.length) {
    newArray.push(list.pop());
  }
  return newArray;
};