#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.forEach(listElement => {
    if (listElement === searchElement) {
      num++;
    }
  });
  return (num);
};
