#!/usr/bin/node

const argv = process.argv.slice(2);

if (argv.length <= 1) {
  console.log(0);
} else {
  // Convert each item in list to int
  const intList = argv.map(x => parseInt(x));
  // Sort in descending order
  intList.sort(function (a, b) { return b - a; });
  // Print second item, second largest item
  console.log(intList[1]);
}
