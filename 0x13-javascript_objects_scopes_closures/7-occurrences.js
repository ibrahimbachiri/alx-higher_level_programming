#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  // Count the occurrences of searchElement in the list
  return list.reduce((count, currentElement) => (currentElement === searchElement ? count + 1 : count), 0);
};
