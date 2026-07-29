# JavaScript: Single-Threaded & Asynchronous

JavaScript is often described as a **single-threaded, non-blocking, asynchronous, concurrent** language. 

## 1. Single-Threaded
JavaScript has only **one Call Stack**. This means it can only execute one piece of code at a time. It executes the code line by line, from top to bottom.

```javascript
console.log("One");
console.log("Two");
console.log("Three");
// Output: One, Two, Three
```
If a function takes a long time to execute (e.g., a massive `for` loop), it will "block" the single thread, freezing the UI.

## 2. Asynchronous & Non-Blocking
To prevent blocking the main thread during heavy operations (like network requests, timers, or file reading), JavaScript relies on its host environment (the Browser or Node.js) to handle asynchronous operations.

When an asynchronous operation starts, JavaScript offloads it to the Web APIs (in the browser) or C++ APIs (in Node.js). Once the operation is complete, a callback is sent back to the queue to be executed.

## 3. How does a single thread handle concurrency?
The magic happens through the combination of the **Call Stack**, **Web APIs**, **Callback Queue / Microtask Queue**, and the **Event Loop**. 

Even though JS itself executes one thing at a time, the runtime environment provides the asynchronous capabilities!
