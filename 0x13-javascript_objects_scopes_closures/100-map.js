#!/usr/bin/node

const data = require('./100-data').list;

const mappedData = data.map((value, index) => value * index);

console.log(data);
console.log(mappedData);
