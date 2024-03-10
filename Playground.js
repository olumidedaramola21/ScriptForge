// Funtion Hoisting
// const createFunction = function () {
//   return f;
//   function f(a, b) {
//     const sum = a + b;
//     return sum;
//   }
// };

// const b = createFunction();
// console.log(b(3, 4));

// CLOSURES........
// function createAdder(a) {
//   function f(b) {
//     const sum = a + b;
//     return sum;
//   }
//   return f;
// }

// const b = createAdder(3);
// console.log(b(4));

// Arrow Function
// const f = (a, b) => {
//   const sum = a + b;
//   return sum;
// };
// console.log(f(3, 4));

// Omit Return
// const f = (a, b) => a + b;
// console.log(f(3, 4));

// Rest syntax
// function f(...args) {
//   const sum = args[0] + args[1];
//   return sum;
// }
// console.log(f(3, 4));

// function log(inputFunction) {
//   return function (...args) {
//     console.log("Input", args);
//     const results = inputFunction(...args);
//     console.log("Output", results);
//     return results;
//   };
// }
// const f = log((a, b) => a + b);
// console.log(f(3, 4));

//  Closure Example
// function createCounter() {
//   let value = 0;

//   function increment() {
//     return ++value;
//   }
//   return {
//     increment: increment,
//   };
// }

// const counter1 = createCounter();
// const counter2 = createCounter();

// console.log(counter1.increment());
// console.log(counter1.increment());

// console.log(counter2.increment());

function charCount(str) {
  // make object to return at end
  var result = {};
  // loop over the string, for each character...
  for (let i = 0; i < str.length; i++) {
    var char = str[i];
    // if the char is a number/letter and is a key in object, add one to count
    if (result[char] > 1) {
      result[char]++;

      //if the char ia s number/letter and not in object, add it to objcet and set value to 1
    } else {
      result[char] = 1;
    }
  }

  // if character is something else (space, period, etc) don't do anything
  // return object at end
  return result;
}

charCount("hello");
