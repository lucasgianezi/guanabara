# DONE layout
# DONE variavel para receber valor das compras
# DONE layout
# DONE variavel para receber forma de pagamento
# DONE condição

print(f'{" LOJA DO GIANEZI " :=^40}')
compras = float(input('Qual o valor das compras? R$ '))
print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    vf = 0.9*compras
elif opcao == 2:
    vf = 0.95*compras
elif opcao == 3:
    vf = compras
    print(f'Sua compra será parcelada em 2x de R${compras/2:,.2f} SEM JUROS')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    vf = 1.2*compras
    print(f'Sua compra será parcelada em {parcelas}x de R${vf/parcelas:,.2f} COM JUROS')
else:
    vf = compras
    print('Opção inválida de pagamento!')

print(f'Sua compra de R${compras:,.2f} vai custar R${vf:,.2f} no final.')
