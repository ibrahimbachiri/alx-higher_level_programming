#!/usr/bin/node

exports.esrever = function (list) {
  // Create a reversed version of the list without using reverse method
  const reversedList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
