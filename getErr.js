var _ = require('lodash');
var $ = require('jquery');
var xlsx = require('node-xlsx');
var err = require('./err');

var data = [];
_.forIn(err, function(value, key) {
  // console.log([key,value]);
  _.concat(data,[key,value]);
  console.log(data);
})
