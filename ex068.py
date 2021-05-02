
# DONE importar biblioteca random para usar randint
# DONE print layout
# DONE variavel contadora de vitorias, inicia com zero
# DONE entra no while com True
# DONE variavel para receber inteiro
# DONE variavel para definir lado
# DONE variavel para o computador escolher o dele
# DONE variavel soma para somar n + pc
# DONE condição if com break caso a soma seja diferente do lado escolhido
# adiciona 1 a vitorias

from random import randint

print('-='*25)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR":^50}')
print('-='*25)

vitorias = 0

while True:
    n = int(input('Digite um valor: '))
    lado = input('Você quer par ou ímpar [P/I]? ')
    pc = randint(0,10)
    soma = n + pc
    print('_'*50)
    print(f'Você jogou {n} e o computador jogou {pc}. Total deu {n+pc} e é', end=' ')
    print('PAR' if soma % 2 ==0 else 'ÍMPAR')
    print('_'*50)

    if (soma % 2 == 0) and (lado in 'Ii'):
        break
    elif (soma % 2 != 0) and (lado in 'Pp'):
        break
    print('VOCÊ VENCEU!')
    print('Vamos jogar novamente...')
    vitorias += 1
    print('-='*25)

print('VOCÊ PERDEU')
print(f'Game Over...Você venceu {vitorias} vez(es)!')
