#!/usr/bin/node

const data = require('./101-data').dict;

const sortedDict = {};

Object.keys(data).forEach(userId => {
  const occurrences = data[userId];

  if (sortedDict[occurrences] === undefined) {
    sortedDict[occurrences] = [userId];
  } else {
    sortedDict[occurrences].push(userId);
  }
});

console.log(sortedDict);
