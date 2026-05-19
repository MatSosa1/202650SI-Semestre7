const miPromesa = new Promise((resolve, reject) => {
  setTimeout(() => {
    const cumple = true;

    if (cumple)
      resolve('La promesa se cumplió');
    else
      reject('La promesa no se cumplió');
  }, 2000);
});

const promesaResuelta = new Promise((resolve, reject) => {
  resolve('Primer Valor de la promesa');
  resolve('Segundo Valor de la promesa');

  reject(new Error('Error en la promesa'));
});
promesaResuelta
.then((value) => console.log(value))
.catch((error) => console.log(error));

console.log(promesaResuelta);
