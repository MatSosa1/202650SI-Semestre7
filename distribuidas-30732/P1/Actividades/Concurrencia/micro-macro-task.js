// // Macro Tasks queue
// setTimeout(() => {
//   console.log('Time 1');
// }, 0);

// setInterval(() => {
//   console.log('Interval 1');
// }, 1000);

// // DOM (Document Object Model)
// // document.addEventListener('click', () => {
// //   console.log('Click Event 1');
// // });

// setInmediate(() => {
//   console.log('Inmediate 1');
// });


// // Micro Tasks queue
// Promise.resolve()
// .then(() => {
//   console.log('Promise 1');
// });

// Promise.resolve()
// .then(() => {
//   console.log('Promise 2');
// });

// queueMicrotask(() => console.log('Microtask 1'));


// Ejemplo Combinado
console.log('Inicio');

setTimeout(() => {
  console.log('Timeout 1')
}, 100);

Promise.resolve()
.then(() => {
  console.log('Promise 1');
});

console.log('Fin');
