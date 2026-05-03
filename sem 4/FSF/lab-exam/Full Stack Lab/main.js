// Importing the func.js module 

// The ./ says that the func module is in the same directory as the main.js file

const f = require('./func'); 

// Require returns an object with add() and stores it in the f variable which is used to invoke the required 

const result = f.add(10, 5); 
console.log('The result is:', result); 
  
console.log('The difference is :',f.subtract(10, 5)); 