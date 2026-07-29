# Closures in JavaScript

A **closure** is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function's scope from an inner function.

Closures are created every time a function is created, at function creation time.

## Example

```javascript
function makeCounter() {
    let count = 0; // 'count' is a local variable created by makeCounter

    return function() { // This inner function is the closure
        count++;        // It has access to 'count' from the outer scope
        return count;
    };
}

const counter = makeCounter();

console.log(counter()); // 1
console.log(counter()); // 2
console.log(counter()); // 3
```

## Why are Closures Useful?

1. **Data Privacy / Encapsulation**: You can create private variables that cannot be accessed directly from the outside, only through the functions returned by the closure.
2. **Currying and Function Factories**: Creating functions that are pre-configured with certain arguments.
3. **Memoization**: Remembering the results of expensive function calls.
4. **State in Asynchronous Callbacks**: Keeping track of state variables across asynchronous operations.

## Lexical Scoping
JavaScript uses lexical scoping. The scope of a variable is determined by its position in the source code. Nested functions have access to variables declared in their outer scope, even after the outer function has returned.
