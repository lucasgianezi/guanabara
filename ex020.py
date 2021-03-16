# variavel para receber o aluno1 DONE
# variavel para receber o aluno2 DONE
# variavel para receber o aluno3 DONE
# variavel para receber o aluno4 DONE
# lista com todos os alunos DONE
# printar lista para check DONE
# embaralhar lista
# print lista emabaralhada

import random

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')

lista = [n1, n2, n3, n4]
#print(lista)
random.shuffle(lista)
#print(lista)
print('A ordem de apresentação será: {}'.format(lista))
