#!/usr/bin/node
/* a script that prints the first argument passed to it */

if (process.argv.legnth < 3) {
console.log();
} else {
console.log(process.argv[2]);
}
