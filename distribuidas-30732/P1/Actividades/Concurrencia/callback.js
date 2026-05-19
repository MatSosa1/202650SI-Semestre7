const numeros = [1, 2, 3];

// numeros.forEach(function (n) {
//   console.log(n);
// });

// numeros.forEach((n) => {
//   console.log(n);
// });

// const dobles = numeros.map((n) => {
//   return n * 2;
// });
// console.log(dobles);

// const pares = numeros.filter((n) => {
//   return n % 2 === 0;
// });
// console.log(pares);

// Callback síncronos
console.log('Before');
[1, 2, 3].forEach((n) => {
  console.log(n);
});
console.log('After');

// Callbacks asíncrono
console.log('Before');

setTimeout(() => {
  console.log('After');
}, 1000);

console.log('Middle');
