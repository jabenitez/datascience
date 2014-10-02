#!/usr/bin/env node

//Prime numbers
//

var isprime = function(n) {
    for(i=2; i < n ; i++){
	if(n%i == 0)
	    return false;
    }
    return true;
};

// FInd first K prime numbers via basic while loop
var firstkprime = function(k) {
    var i = 2;
    var check = 1;
    var arr = [];
    
    while(check < k+1) {
	if(isprime(i)){
	    arr.push(i);
	    check++;
	}
	i++;
    }
    return arr;
};

// Print to console
var pmt = function(arr) {
    return arr.join(",");
};

var k = 100;
var fs = require('fs');
var outfile = "primes.txt"
fs.writeFileSync(outfile, pmt(firstkprime(k)))
console.log("firstkprime(" + k + ")");
console.log(pmt(firstkprime(k)));

