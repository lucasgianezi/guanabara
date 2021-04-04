# DONE da biblioteca random importar randint
# DONE computador escolhe um inteiro entre 1 e 10
# DONE jogador escolhe numero
# DONE criar variável para fazer contagem das tentativas
#  condição while

from random import randint

jogador = int(input('Digite um número: '))

cont = 1

while jogador != num:
    cont += 1

    if num > jogador:
        jogador = int(input('Maior. Digite outro número: '))
    else:
        jogador = int(input('Menor. Digite outro número: '))
      

print(f'Parabéns, você acertou o número. Foram necessárias {cont} tentativa(s)!')
