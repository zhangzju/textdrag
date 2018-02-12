var _ = require('lodash');
var $ = require('jquery');
var xlsx = require('node-xlsx');
var fs = require('fs');

//data area
var data = fs.readFileSync("source/help.js");

//handle
const reg = /\"(.*?)\"/g;

var str = data.toString();
function getStr(str) {
    var result = str.match(/\"\w*\"/g);
    return result.map(function(element){
        return element.replace(/\"/g, '');
    });
}

var res = getStr(str).map(function (item,index,input) {
    return item*10;
 })