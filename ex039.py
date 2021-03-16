# DONE variavel para receber o ano de nascimento
# calcular a idade que ele tem no ano atual
# comparar idade com 18
# fazer condição aninhada

import datetime

ano = int(input('Digite o ano de nascimento: '))
#print(ano)

ano_atual = datetime.date.today().year
idade = ano_atual - ano

print(f'Quem nasceu em {ano} tem {idade} anos em {ano_atual}.')

if idade < 18:
    print('Ainda faltam {} anos para o alistamento.'.format(18-idade))
    print(f'Seu alistamento será em {ano_atual+(18-idade)}')
elif idade == 18:
    print('Seu alistamento será esse ano.')
else:
    print('Já se passaram {} anos do seu alistamento'.format(idade-18))
    print(f'Seu alistamento foi em {ano+18}.')
