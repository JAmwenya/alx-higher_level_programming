#!/usr/bin/node

/* a script that prints x times “C is fun”
 * Where x is the first argument of the script */

const x = process.argv[2];
let i = 0;

if (x === undefined || isNaN(x) || x <= 0) {
  console.log("Missing number of occurrences");
} else {
  for (i = 0; i < x; i++) {
    console.log("C is fun");
  }
}
