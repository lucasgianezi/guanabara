# variavel para receber o nome do aluno1
# variavel para receber o nome do aluno2
# variavel para receber o nome do aluno3
# variavel para receber o nome do aluno4
# variavel para receber o nome do aluno sorteado

from random import choice

lista = []

aluno1 = input('Nome do aluno1: ')
lista.append(aluno1)
aluno2 = input('Nome do aluno2: ')
lista.append(aluno2)
aluno3 = input('Nome do aluno3: ')
lista.append(aluno3)
aluno4 = input('Nome do aluno4: ')
lista.append(aluno4)

sorteado = choice(lista)

print(f'O aluno escolhido foi: {sorteado}')