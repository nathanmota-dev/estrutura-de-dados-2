Repositório para armazenar os trabalhos da disciplina de Estruturas de Dados 2, onde foi apresentado alguns algortimos muito conhecidos e utilizados na computação e o objetivo é entender como eles funcionam e como são implementados. 

## Implementação
- [Busca Binária e Busca sequencial](/trabalho-01/exc1.py)
- [Algoritmo Naive String Matcher](/trabalho-02/exc1/exc1.c)
- [Algoritmo RabinKarp Matcher](/trabalho-02/exc2/exc2.c)
- [Algoritmo de Huffman](/trabalho-03/main.py)
- [Pesquisa binária recursiva 1](/trabalho-04/exc1.py)
- [Pesquisa binária recursiva 2](/trabalho-04/exc2.py)
- [DFS e BFS](/trabalho-05/main.py)
- [Algoritmo de Dijkstra](/trabalho-06/main.py)
- [Algoritmo de Hopcroft-Karp](/trabalho-07/main.c)
- [Algoritmo de Boruvka](/trabalho-08/main.c)

## Trabalho 1 - Busca Binária e Busca Sequencial

## Busca Binária

A Busca Binária precisa de um vetor pré-ordenado para funcionar, ela é um algoritmo de busca que divide o vetor em duas partes e verifica se o elemento que está sendo procurado está na parte esquerda ou direita do vetor.

Vamos supor que a gente tem uma lista com 7 elementos sendo eles: 0,2,3,5,7,8,9 e estamos buscando a igualdade do elemento 7. A gente vai dividir o vetor em duas partes e verificar se o elemento 7 está na parte esquerda ou direita do vetor.

Como a lista é de número ímpar, a gente pega o elemento do meio da lista e verifica se esse elemento é igual a 7. Se for igual a 7, a busca termina. Se não for igual a 7, a gente verifica se o elemento do meio é maior ou menor que 7. 

Nesse caso o elemento central da lista é 5, como 5 é menor que 7, a gente vai pegar a parte direita da lista e fazer a mesma coisa. A gente vai pegar o elemento do meio da lista e verificar se ele é igual a 7. Se for igual a 7, a busca termina. Se não for igual a 7, a gente verifica se o elemento do meio é maior ou menor que 7.

No caso o elemento central é 8 e identificamos que o elemento é menor que 8, portanto só pode ser 7 e a busca termina.

Se a lista for par, a gente pega o primeiro elemento da lista mais o elemento do meio+1 e verifica se o elemento que está sendo procurado é igual a algum desses elementos. Se for igual a algum desses elementos, a busca termina. Se não for igual a nenhum desses elementos, a gente verifica se o elemento do meio é maior ou menor que o elemento que está sendo procurado.

Exemplo: Lista com 6 elementos: 1,2,3,4,5,6. Estamos buscando o elemento 6. A gente pegaria (1+4)/2=2.5 ou apenas 2. Como 6 é maior que 2, a gente pega a parte direita da lista e faz a mesma coisa. A gente pega o elemento do meio da lista que é 5 e verifica se ele é igual a 6. Como não é igual, é maior e só temos um elemento concluimos que o elemento é 6.

## Busca Sequencial

A Busca Sequencial é um algoritmo de busca que percorre o vetor do início ao fim verificando se o elemento que está sendo procurado é igual ao elemento que está sendo percorrido.

Vamos supor que a gente tem um vetor com 6 elementos sendo eles: 10, 43, 76, 5, 13, 24 e estamos buscando a igualdade do elemento 13. A gente vai percorrer o vetor do início ao fim verificando se o elemento que está sendo percorrido é igual ao elemento 13.

Comparando com a Busca Binária, a Busca Sequencial é mais lenta, porque no seu pior caso ela vai percorrer o vetor inteiro para encontrar o elemento que está sendo procurado.

## Trabalho 2 - Algoritmo Naive String Matcher e Algoritmo Rabin Karp Matcher

## Algoritmo Naive String Matcher

O Algoritmo de Naive String Matcher serve para conseguir achar um padão de uma substring dentro de uma string.

Ele funciona comparando a substring com a string, se a substring for igual a string, ele retorna a posição da string onde a substring foi encontrada. Caso não seja igual ele avança uma posição e compara novamente.

Exemplo: String = "ABACADABCAC", Substring = "ABC". Ele compara ABC com as 3 primeiras posições da String que é ABA, como não é igual ele avança uma posição e compara BAC com ABC, como não é igual ele avança uma posição e compara ACA com ABC, como não é igual ele avança uma posição e compara CAD com ABC, como não é igual ele avança uma posição e compara ADB com ABC, como não é igual ele avança uma posição e compara DAB com ABC, como não é igual ele avança uma posição e compara ABC com ABC, como é igual ele retorna a posição 7.

## Algoritmo Rabin Karp Matcher

O Algoritmo de Rabin Karp Matcher também é um algoritmo de busca de substring que utiliza o método de hashing para encontrar a substring.

Ele funciona calculando o hash da substring e comparando com o hash da string, se os hashes forem iguais ele compara a substring com a string, se a substring for igual a string, ele retorna a posição da string onde a substring foi encontrada. Caso não seja igual ele avança uma posição e recalcula o hash da substring e compara novamente.

Mesmo que o hash for igual ele compara a substring com a string, porque pode ter ocorrido uma colisão.

O Algoritmo de Rabin Karp Matcher é melhor que o Algoritmo de Naive String Matcher nos casos em que a substring é muito grande, porque ele calcula o hash da substring e compara com o hash da string, enquanto o Algoritmo de Naive String Matcher compara a substring com a string. Além disso ele é mais rápido que o Algoritmo de Naive String Matcher.

## Trabalho 3 - Algoritmo de Huffman

O Algoritmo de Huffman é uma técnica de compressão de dados sem perda. Funciona contando a frequência de cada caractere em uma string de entrada para criar uma árvore binária de Huffman. A árvore é construída a partir de nós folhas, que representam cada caractere com sua frequência. Os nós internos representam a soma das frequências dos nós filhos, formando uma estrutura binária.

Por exemplo, na string "ABRACADABRA", as frequências são: A = 5, B = 2, R = 2, C = 1, D = 1. Os nós são organizados com base nessas frequências.

A árvore de Huffman é construída combinando os dois nós de menor frequência repetidamente até restar apenas um nó, que é a raiz da árvore e representa a soma de todas as frequências.

Os códigos binários para cada caractere são determinados percorrendo a árvore de Huffman. Caracteres mais frequentes recebem códigos mais curtos, enquanto caracteres menos frequentes recebem códigos mais longos.

## Trabalho 4 - Pesquisa binária recursiva

O algoritmo de Pesquisa binária recursiva é um algoritmo de busca que divide o array (vetor) em duas partes e verifica se o elemento que está sendo procurado está na parte esquerda ou direita do array em relação ao meio. Se o elemento estiver na metade correta, o algoritmo prossegue a busca apenas nessa metade.

A principal diferença entre a Pesquisa binária recursiva e a Pesquisa binária iterativa é que a recursiva utiliza recursão para chamar a função novamente com os novos limites de busca (início e fim) definidos. Isso permite que o algoritmo continue dividindo o intervalo de busca pela metade até encontrar o elemento ou concluir que ele não está presente.

Embora a abordagem recursiva possa ser mais elegante em termos de código, ela pode ser menos eficiente em termos de uso de memória (por causa da pilha de recursão) em comparação com a implementação iterativa. No entanto, ambas têm a mesma eficiência em termos de tempo de execução, com complexidade de tempo de O(log n), onde n é o número de elementos no array.

## Trabalho 5 - DFS e BFS

## BFS - Breadth First Search

O algoritmo de busca em largura (BFS) é um algoritmo de busca que percorre um grafo com o objetivo de encontrar o caminho mínimo entre dois vértices ou explorar todos os vértices e arestas de um grafo. O algoritmo utiliza uma fila (queue) para armazenar vértices a serem explorados. Inicia-se no vértice de origem e visita todos os vértices vizinhos antes de avançar para os vértices do próximo nível de distância. Assim, o BFS percorre o grafo por camadas ou níveis de distância, garantindo que todos os vértices sejam explorados na menor distância possível.

Basicamente ele percorre todos os vértices que estão em um mesmo nível antes de passar para o próximo nível. Esse algortimo funciona tanto para grafos direcionados como para grafos não direcionados.

A medida que eu vou caminhando no grafo eu vou colocando cores nos meus vértices, sendo elas: Branco, Cinza e Preto. O Branco é o vértice que ainda não foi visitado, o Cinza é o vértice que foi visitado mas ainda não foi explorado e o Preto é o vértice que foi visitado e explorado.

O vértice inicial começa com a cor cinza (já foi visitado), a sua distância 0 por ser o vértice pai e seu antecessor é nulo.
A fila (FIFO) serve para colocar os vértices

## DFS - Depth First Search

O algoritmo de busca em profundidade (DFS) é um algoritmo de busca que percorre um grafo explorando o mais profundamente possível em cada caminho antes de retroceder. O algoritmo utiliza uma pilha (stack) ou recursão para armazenar vértices a serem explorados. Ele começa no vértice de origem e visita um caminho até o final antes de voltar e explorar outros caminhos. Isso faz com que o DFS seja útil para detectar ciclos, encontrar componentes conectados, e, em alguns casos, resolver problemas de percurso e ordenação topológica.

Ele funciona da seguinte forma: vamos supor que a gente tem um grafo onde a gente sai da raiz e o proximo nível tem 2 vertices, o próximo próximo tem 2 vertices e o próximo próximo próximo tem 2 vertices também. Ele sai da raiz, vai pro primeiro nível pela esquerda, vai pro segundo nivel pela esquerda, vai pro terceiro nivel pela esquerda e identifica que não tem como mais pra onde ir, então ele retorna um nível e para isso ele utiliza pilha, pra conseguir guardar os vertices que ele já visitou, então retornando de nível ele vai pra direita e visita, como não tem mais pra onde ir ele retorna um nível e vai pra direita e assim por diante.

## Trabalho 6 - Algoritmo de Dijkstra

O Algoritmo de Dijkstra funciona para encontrar o menor caminho entre dois vértices de um grafo ponderado. Ele utiliza uma fila de prioridade para armazenar os vértices a serem explorados, priorizando os vértices com menor custo. Inicia-se no vértice de origem e explora todos os vértices vizinhos, atualizando o custo mínimo para alcançar cada vértice. O algoritmo continua até que todos os vértices tenham sido explorados e o menor caminho para o vértice de destino seja encontrado.

## Trabalho 7 - Algoritmo de Hopcroft-Karp

O Algoritmo de Hopcroft-Karp utiliza busca em largura (BFS) e busca em profundidade (DFS) para encontrar o emparelhamento máximo em um grafo bipartido. Um grafo bipartido é uma estrutura em que os vértices são divididos em dois conjuntos distintos, e todas as arestas conectam vértices de conjuntos diferentes. O emparelhamento máximo busca o maior conjunto de arestas que não compartilham vértices finais, maximizando assim os pares de vértices emparelhados.

Considere um grafo bipartido com seis vértices em cada conjunto e múltiplas arestas entre eles. O objetivo é encontrar o maior emparelhamento possível, emparelhando todos os vértices do conjunto esquerdo com os vértices do conjunto direito.

O algoritmo funciona assim: primeiramente, é usado BFS para estabelecer os níveis dos vértices livres, ou seja, a distância entre os vértices livres de conjuntos opostos. Em seguida, é utilizado DFS para encontrar caminhos aumentadores. Um caminho aumentador começa em um vértice livre de um conjunto, alterna entre vértices emparelhados e livres, e termina em um vértice livre no outro conjunto.

Quando um caminho aumentador é encontrado, o emparelhamento atual é atualizado para incluir o novo caminho, aumentando assim o emparelhamento máximo. O processo é repetido alternando entre BFS e DFS até que não haja mais caminhos aumentadores disponíveis. Assim, o algoritmo Hopcroft-Karp permite encontrar o maior emparelhamento possível de forma eficiente.

## Trabalho 8 - Algoritmo de Boruvka

Arvore Geradora Minima - Algoritmo de Boruvka

Vamos imaginar que uma Compania de Distruibuição de agua quer abastecer: A,B,C,D,E e F conforme o grafo abaixo:

[Grafo 1](/trabalho-08/assets/grafo1.JPG)

Para aplicar o Algoritmo de Boruvka basicamente vamos precisar seguir alguns passos:

1º Passo: Remover todas as arestas paralelas (mais de uma conexão) e ciclos

[Grafo 2](/trabalho-08/assets/grafo2.JPG)

2º Passo: Iniciar com um grafo parcial, o grafo T constíuído por todos os vértices e da respectivas arestas de menor valor que emanam (saem) dos mesmos

[Grafo 3](/trabalho-08/assets/grafo3.JPG)

3º Passo: Agrupar os vertices sucessivamente pelas arestas de menor valor identificados desde que não forme um circuito

E-D=2
E-F=2
C-B=3
C-E=3
D-F=4 -> Forma um circuito então não é adicionada
A-B=7

[Grafo 4](/trabalho-08/assets/grafo4.JPG)

Então assim o algoritmo de Boruvka foi aplicado gerando a Arvore Geradora Mínima. 

[Grafo 5](/trabalho-08/assets/grafo5.JPG)

Sendo assim iria gastar para percorrer todo percurso:

7+3+3+2+2 = 17.

A implementação do algoritmo de Boruvka foi feita em C e pode ser acessada [aqui](/trabalho-08/main.c)