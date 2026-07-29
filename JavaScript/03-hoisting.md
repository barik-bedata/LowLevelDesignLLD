# Hoisting in JavaScript

**Hoisting** is JavaScript's default behavior of moving declarations to the top of the current scope (the current script or the current function) before code execution. 

It is important to note that only the **declarations** are hoisted, not the **initializations**.

## 1. Variable Hoisting (`var`, `let`, `const`)

### `var`
Variables declared with `var` are hoisted to the top and initialized with `undefined`.
```javascript
console.log(myVar); // Output: undefined (no error!)
var myVar = 10;
console.log(myVar); // Output: 10
```

### `let` and `const`
Variables declared with `let` and `const` are also hoisted, but they are **NOT** initialized. Accessing them before initialization results in a `ReferenceError`. The period between entering the scope and the actual declaration is called the **Temporal Dead Zone (TDZ)**.
```javascript
console.log(myLet); // ReferenceError: Cannot access 'myLet' before initialization
let myLet = 20;
```

## 2. Function Hoisting

### Function Declarations
Function declarations are completely hoisted. You can call the function before it appears in the code.
```javascript
greet(); // Output: "Hello"

function greet() {
    console.log("Hello");
}
```

### Function Expressions (and Arrow Functions)
If you assign a function to a variable (`var`, `let`, `const`), it follows the variable hoisting rules instead.
```javascript
sayHi(); // TypeError: sayHi is not a function (it's undefined because of var)

var sayHi = function() {
    console.log("Hi");
};

sayArrow(); // ReferenceError: Cannot access 'sayArrow' before initialization
const sayArrow = () => console.log("Arrow");
```
