#!/usr/bin/node
// A script

const args = process.argv;
let request = require('request');
request(args[2], function (error, response, body) {
  if (error) {
    console.log('error:', error); // Print the error if one occurred
  } else console.log('code:', response && response.statusCode);
});
