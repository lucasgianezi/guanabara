# DONE variavel para receber o salario
# condição

salario = float(input('Qual o salário? '))

if salario <= 1250:
    print('O novo salário será R${:,.2f}'.format(salario*(1.15)))
else:
    print(f'O novo salário será R${salario*(1.10):,.2f}')
    