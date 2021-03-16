# DONE variavel para receber o input da velocidade
# DONE print para check
# condicional
# print dirija com segurança


velocidade = float(input('Qual a velocidade? '))
#print(velocidade)
if velocidade <= 80:
    print('Continue assim. Dirija com segurança!')
else:
    print('Você está acima da velocidade!')
    print(f'Deverá pagar uma multa de R${(velocidade-80)*7:.2f}')
    print('Não continue assim. Dirija com segurança!')
    