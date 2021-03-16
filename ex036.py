# DONE variavel para receber valor da casa
# DONE varia para receber salario
# DONE variavel para receber prazo de pagamento
# DONE calculo da prestação
# condição: se prestação maior que 30% do salario, emprestimo concedido, else negado


casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o salário? '))
tempo = int(input('Você vai pagar em quanto tempo? '))

prestacao = casa/(tempo*12)
print('Para pagar uma casa de R${:,.2f} em {} anos a prestação será de R${:,.2f}.'.format(casa, tempo, prestacao))

if prestacao <= 0.3*salario:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')
