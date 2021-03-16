
# DONE import random
# DONE variavel para receber um inteiro randomico entre 1 e 5
# DONE variavel para armazenar o input do usuario escrever um numero inteiro entre 1 e 5
# DONE fazer a condição simples

import random
import time

num = random.randint(1, 5)

usuario = int(input('Digite um inteiro entre 1 e 5: '))
print('PROCESSANDO...')
time.sleep(3)
print("Você digitou o número {}".format(usuario))
print(f'O computador tinha escolhido {num}')

if usuario is num:
    print("Você acertou!")
else:
    print('Você errou!')
