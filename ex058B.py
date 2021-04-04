# DONE da biblioteca random importar randint
# DONE fazer o computador pensar em número
# criar variavel para contar as tentativas

from random import randint

computador = randint(1,10)
cont = 0
acertou = False

while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    cont += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Mais')
    else:
        print('Menos')

print(f'Acertou! Foram necessárias {cont} tentativas!')
