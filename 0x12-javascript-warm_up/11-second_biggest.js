#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  // Convert from array of strings to array of numbers
  const numbersArray = process.argv.slice(2).map(function (str) {
    return parseInt(str);
  });
  // Sort in descending order
  numbersArray.sort(function (a, b) {
    return b - a;
  });
  console.log(numbersArray[1]);
}
