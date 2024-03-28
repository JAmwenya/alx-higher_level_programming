#!/usr/bin/node
/* a script that prints 3 lines by using an array of string and a loop */
const fun = 'C is fun';
const cool = 'Python is cool';
const amazing = 'JavaScript is amazing';
let i = 0;

const myList = [fun, cool, amazing];
while (i < myList.length) {
  console.log(myList[i]);
  i++;
}
