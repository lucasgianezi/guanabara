# DONE variavel para receber o ano
# DONE print para check
# DONE fazer condição para múltiplo de 4, mas não multiplo de 100 ou multiplo de 400
# pegar ano da máquina

import datetime


ano = int(input('\nDigite o ano: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano%400 == 0:
    print(f'O ano {ano} é bissexto!')
else:
    print('O ano {} não é bissexto!'.format(ano))
