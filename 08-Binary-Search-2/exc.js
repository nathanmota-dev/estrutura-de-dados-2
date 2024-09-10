function buscaBinariaRecursiva(lista, alvo, inicio, fim) {

  if (inicio > fim) {
    return false;
  }

  // Calcula o índice do meio da lista
  let meio = Math.floor((inicio + fim) / 2);


  if (lista[meio] === alvo) {
    return true;
  }

  if (lista[meio] > alvo) {
    return buscaBinariaRecursiva(lista, alvo, inicio, meio - 1);
  }

  return buscaBinariaRecursiva(lista, alvo, meio + 1, fim);
}

const listaOrdenada = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
const alvo = 7;
const encontrado = buscaBinariaRecursiva(listaOrdenada, alvo, 0, listaOrdenada.length - 1);

console.log(encontrado ? `O número ${alvo} foi encontrado.` : `O número ${alvo} não foi encontrado.`);