



frase = '   Renda       234 Fixa com Python'

# --------FATIAMENTO----------

print(frase[9])
print(frase[1:5])
#print(frase[21]) #isso dá erro pois len(frase) == 21

print(frase[9:22]) # isso não vai trazer erro mas não é uma boa opção colocar um indice que não existe

print(frase[1:20:2])

print(frase[:5]) # se omitir o inicio ele pega desde 0. portanto, é bom usar quando vc quer ir até tal indice, pegando desde o começo

print(frase[6:]) # se omitir o fim ele considera o ultimo caractere msm, vale a pena usar se vc quer começar a partir de um caractere e ir até o final, assim vc não precisa indicar qual o final

print(frase[5::3]) # pega desde 5, até o final, pulando de 3 em 3

# --------- ANÁLISE --------------

print(len(frase)) # len vem de length, len conta os espaços sim

print(frase.count(' ')) # contagem sem fatiamento, considerando toda a string

print(frase.count('a', 0, 6)) # contagem com fatiamento

print(frase.find('a')) # find acha o indice de onde começa a palavra, se a palavra aparece mais de 1 vez ele traz o indice da primeira ocorrencia

print(frase.find('w')) # se palavra que queremos achar o indice não existir na string , ele trara o valor -1.

print("Renda" in frase) # variavel booleana que retorna True/false se a palavra estiver na string ***ATENÇÃO: ELE NÃO RETORNA O INDICE, APENAS TRUE OU FALSE.*** Acho que eu já vi codigos que misturam isso com find IF palavra in FRASE: frase.find("palavra")

# ----------TRANSFORMAÇÃO------------
"""
via de regra uma string é imutável, por exemplo eu não consigo fazer frase[4] = o -> "Rendo"
o erro que dá é: 'str' object does not support item assignment.
Isso já é suficiente para questionar o item que estamos falando agora que é 'Transformação'. o que podemos transformar se strings são imutaveis?

Na verdade eu não consigo mexer nos elementos, mas eu consigo mudar atravez de métodos
mas essa mudança é momentanea
para deixar gravado temos que sobrescrever a variável ou associar a uma outra variavel
é feita uma identação nova com as alterações tanto se alteramos temporariamente atraves do metodo ou se associamos a uma nova variavel"""
frase = frase.replace('Renda', 'FX') 
print(frase.replace('Renda', 'FX'))
print(frase)

print(frase.upper()) # transforma todas as letras que a string tem em maiusculas, numeros e espaçoes obviamente ficam intactos
print(frase.lower()) # contrario de upper
print(frase.capitalize()) # todas as letras ficam minusculas e a primeira letra somente da primeira palavra de toda a string fica como maiuscula
print(frase.title()) # todas as letras ficam minusculas e a primeira letra de todas as palavras ficam como maiuscula, ele faz essa analise com os espaços. onde tiver espaço ele identifica como palavra

print(frase.strip()) # retira todos os espaços se houver antes do primeiro caractere e depois do ultimo

print(frase.rstrip()) # retira todos os espaços se houver depois do ultimo caractere (não tira os espaços antes do primeiro caractere)

print(frase.lstrip()) #retira todos os espaços se houver antes do primeiro caractere (não retira os espaçoes depois do ultimo caractere)

# -----------DIVISÃO------------
""" Mesmo raciocinio dos metodos acima de transformação
'Na verdade eu não consigo mexer nos elementos, mas eu consigo mudar atravez de métodos
mas essa mudança é momentanea
para deixar gravado temos que sobrescrever a variável ou associar a uma outra variavel'
é feita uma identação nova com as alterações tanto se alteramos temporariamente atraves do metodo ou se associamos a uma nova variavel
"""

frase = '      Renda    Fixa com Python'

print(frase.split()) # retira todos os espaços antes do primeiro caracter, todos os espaçoe entre os caracteres e todos os espaçoes depois do ultimo caracter retorna uma lista com os caracteres somente. Cada palavra recebe indexação nova. cada item da lista é uma palavra que estava separada por espaços na string.

print(frase.split()[1][1])

print(frase)

# -----------JUNÇÃO------------

print('-'.join(frase.split())) # aparentemente não é colocado nenhum caracter antes da primeira ocorrencia e nem depois da útlima

