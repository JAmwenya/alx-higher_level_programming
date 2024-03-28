#!/usr/bin/node
/* a script that prints My number: <first argument converted in integer> if the
 * first argument can be converted to an integer
 */
const castToInt = parseInt(process.argv[2]);

if (!isNaN(castToInt)) {
  console.log('myNumber: ' + castToInt);
} else {
  console.log('Not a number');
}
