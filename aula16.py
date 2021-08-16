'''
Em Python existem 3 tipos de variáveis compostas: Tuplas, listas e dicionarios.

Uma variável quando é declarada ela vira um espaço na memória.
Eu não preciso atribuir. Só de declarar (declarar é escrever "variável =", "=" é o sinal de atribuição) já vira um espaço na memória.
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
No caso de uma variável composta (seja ela, tupla, lista, dicio e string) eu tenho varios elementos. Se eu me referir a variavel eu estarei me referindo ao conjunto de elementos. Então só poderia usar funções que tratassem do conjunto.
Mas é possível eu acessar algum elemento específico do conjunto? Sim, é possível.

Os elementos de varivaeis compostas (tuplas, listas, dicionarios, strings) são acessados por indices. Os indices são numéricos e começam no zero.

se você se referir a variavel, estará se referindo a todos os elementos, a variavel é o conjunto de todos os elementos.
Os elementos individuais devem ser acessados por indice.Esses indices vão montar a variavel composta.

Conforme vimos no mundo 1, se quisermos acessar letras/elementos de uma string devemos utilizar indices. Que é exatamente a forma de acessar elementos de uma variavel composta.
Na verdade, strings são variáveis compostas. Strings não são tuplas, strings são listas. Mas o ponto é que podemos acessar elementos de uma tupla igual de uma string.
Podemos também fazer fatiamento de tuplas igual fizemos de strings.

Na verdade, essas funções de acessar indices/fatiamento não são propriedades de tuplas e string. São propriedades das variáveis compostas no geral. Como strings e tuplas são variaveis compostas, nós podemos utilizar estes métodos.
Outras funções de variáveis compostas que podem ser usadas com tuplas: len, estrutura de repetição for, count, index, ...
no caso do index, o programa vai pegar sempre a primeira ocorrência.
caso vc queira a segunda ocorrência, você pode colocar um condição para que ele começe a procurar a partir de um determinado indice.
index('letra/número procurado' , a partir de qual posição)

Uma característica importante das tuplas é o fato de elas serem IMUTÁVEIS. Depois de declarar uma tuplas, eu não posso atribuir coisas aos elementos dela. Eu não posso substituir os elementos, não posso aumentar a quantidade de elementos, não posso diminuir, ... Para fazer isso seria preciso criar uma nova tupla.
Se você tentar atribuir um valor a um elemento receberá o erro -> "TypeError: 'tuple' object does not support item assignment"
(O Replace é um método que nem poderíamos usar pois é um método das string] 

As tuplas nós colocamos entre parenteses () ou sem (se vc deixar sem parenteses ele vai considerar uma tupla)
As listas nós colocamos entre colchetes []
Os dicionários nós colocamos entre chaves {}

Os elementos destas estruturas nós separamos por virgula


Uma tupla pode conterdiversos tipos de dados: números, string, booleana, ...
A única forma de mudar uma tupla é através do "del"
se você definir um tupla, fazer um del e depois tentar imprimir a tupla
vc receberá uma mensagem de erro dizendo NameError: name 'pessoa' is not defined

Formas de usar estrutura de repetição:

lanche = ('Hamburguer','suco','bata frita','pizza','pudim','batata frita')

for cont in range(0, len(lanche)):
    print('Eu vou comer {lanche[cont]})

for c in lanche:
    print('Eu vou comer {c})


Formas de usar estrutura de repetição (COM POSIÇÃO):

for cont in range(0, len(lanche)):
    print('Eu vou comer {lanche[cont]} na posição {cont})

for pos, comida in enumerate(lanche):
    print('Eu vou comer {comida} na posição {pos})


como dito anteriormente, uma tupla é imutável.
se fizermos print(sorted(tupla)) isso não vai mudar a ordem da tupla, vai somente mostrar a tupla em ordem. Tanto que essa tupla em ordem aparecerá entre colchetes, e não entre parenteses. pois na verdade vai meio que fazer uma lista temporária.
a tupla continua com o mesmo formato.


Outra coisa que podemoz fazer é "adição de tuplas"
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
c = (2,5,4,5,8,1,2)

Note que ele segue a ordem.
Portanto, nestes casos de adição de tuplas a ordem importa e, portanto, "c = a + b" é diferente de "c = b + a".

portfolio = ('fx', 'rates', 'equities', 'volatility')
print(sorted(portfolio))
print(portfolio)

a = (2,5,4)
b = (5,8,1,2)
c = b + a
print(c)

print(len(c))
print(a.count(8))
print(c.index(8))
'''

c = ('aula')
print(len(c))
del(c)
print(c)