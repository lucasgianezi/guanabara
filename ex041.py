# variavel para receber o ano de nascimento

# condição
from datetime import date as dt

ano = int(input('Digite o ano de nascimento: '))
idade = dt.today().year - ano
print(f'O atleta tem {idade} anos.')

if idade <= 9:
    classificacao = 'Mirim'
elif idade <= 14:
    classificacao = 'Infantil'
elif idade <= 19:
    classificacao = 'Junior'
elif idade <= 20:
    classificacao = 'Sênior'
else:
    classificacao = 'Master'

print(f'Classificação: {classificacao}')
