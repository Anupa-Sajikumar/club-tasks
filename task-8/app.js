const pokedex = document.getElementById('pokedex');

const fetchPokemon = async() => {
        const url = 'https://pokeapi.co/api/v2/pokemon' ;
        const result = fetch(url).then((res)=>res.json())
        result.then(result=>{
            result.results.map((async pokemon=>{
                fetch(pokemon.url).then( async (pokemonDetails) => {
                  const fetchPokemon = await pokemonDetails.json()
                  const innerHtml = `
                  <li class="card">
                  <img class="card-image" src="${fetchPokemon.sprites.front_default}"/>
                  <h2 class="card-title">${fetchPokemon.id}. ${fetchPokemon.name}</h2>
                  <p class="card-subtitle">Type: ${(fetchPokemon.types.map(type=>type.type.name))}</p>
                    </li>
                   `
                    pokedex.innerHTML += innerHtml
                })
              
            }))
        })
};
fetchPokemon();
