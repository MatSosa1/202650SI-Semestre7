function getPokemon(id) {
  return fetch(`https://pokeapi.co/api/v2/pokemon/${id}`)
    .then((res) => {
      if (!res.ok)
        throw new Error('Error al obtener el pokemon');

      return res.json()
    });
}

getPokemon(-1)
  .then((pokemon) => {
    console.log(pokemon.forms);
  })
  .catch((error) => {
    console.log('Pokemon no encontrado: ', error.message);
  });
