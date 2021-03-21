# DONE print do layout
# DONE variavel para receber a jogada
# DONE print do layout
# DONE sortear jogada do computador
# DONE printar de novo jogada do participante
# fazer condição

from time import sleep
import random

print('''
Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))

sleep(1)
print("\nJO")
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print('-='*15)
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = random.randint(0,2)
print('O computador jogou', lista[computador])
print('O jogador jogou', lista[jogador])
print('-='*15)


if computador == jogador:
    print('Ninguém venceu. EMPATE!')
else:
    if computador == 0:                  #computador jogou PEDRA
        if jogador == 1:
            print('JOGADOR VENCE!')
        else:
            print('COMPUTADOR VENCE!')
    elif computador == 1:                 # computador jogou PAPEL
        if jogador == 0:
            print('COMPUTADOR VENCE!')
        else:
            print('JOGADOR VENCE!')
    elif computador == 2:                   # computador jogou TESOURA
        if jogador == 0:
            print('JOGADOR VENCE!')
        else:
            print('COMPUTADOR VENCE!')
