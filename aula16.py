portfolio = ('fx', 'rates', 'equities', 'volatility')
print(portfolio)

'''
Em Python existem 3 tipos de variáveis compostas: Tuplas, listas e dicionarios.

Uma variável quando é declarada ela vira um espaço na memória.
Eu não preciso atribuir. Só de declarar (declarar é escrever "variável =") já vira um espaço na memória.
Toda variável simples é um espaço na memória. Somente 1 espaço.
Quando eu faço a atribuição, o espaço criado na memória quando declaramos a variável é preenchido com o item atribuido.

Por ser uma variável simples só cabe 1 item atribuido.
É por isso que quando tentamos atribuir um novo item, o item antigo é apagado e o novo item fica como o item atribuido. Pq só tem 1 espaço. Se a variável fosse composta eu poderia atribuir mais de 1 item para a variavel.

É possível ter mais de 1 item atribuido a uma variável?
Sim, neste caso precisariamos de uma variável que pudesse ter mais de 1 espaço na memória. Portanto, uma variável composta pode ter mais de 1 espaço na memória.

Variaveis simples só cabe 1 coisa dentro.
Variáveis compostas podem armazenar vários valores.

E dentro do Python existem 3 tipos de variáveis compostas como já foi dito:
Tuplas, listas e dicionários.

Ok. Se temos uma variável com varios elementos. Como posso acessar os elementos dela?
Pq no caso das variáveis simples, a variável é o proprio elemento. Se eu estou me referindo a variavel, eu estou me referindo ao elemento que eu atribui a ela.
No caso de uma variável composta eu tenho varios elementos. Se eu me referir a variavel eu estarei me referindo ao conjunto de elementos. Então só poderia usar funções que tratassem do conjunto.
Mas é possível eu acessar algum elemento específico do conjunto? Sim, é possível.

Os elementos são acessados por indices. Os indices são numéricos e começam no zero.

se você se referir a variavel, estará se referindo a todos os elementos, a variavel é o conjunto de todos os elementos.
Os elementos individuais devem ser acessados por indice.Esses indices vão montar a variavel composta.

Conforme vimos no mundo 1, se quisermos acessar letras/elementos de uma string devemos utilizar indices. Que é exatamente a forma de acessar elementos de uma variavel composta.
Na verdade, strings são variáveis compostas. Strings não são tuplas, strings são listas. Mas o ponto é que podemos acessar elementos de uma tupla igual de uma string.
Podemos também fazer fatiamento de tuplas igual fizemos de strings.

Na verdade, essas funções de acessar indices/fatiamento não são propriedades de tuplas e string. São propriedades das variáveis compostas no geral. Como strings e tuplas são variaveis compostas, nós podemos utilizar estes métodos.

'''