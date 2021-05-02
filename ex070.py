# DONE print layout
# DONE inicio de variaveis (com valor zero) antes de entrar no while
# DONE soma dos preços, qtty de $ mais de 1000, prod mais barato, cont
# DONE while true
# DONE variável recebe nome do produto
# DONE variável para receber preço
# DONE ifs
# DONE variavel de decisão com while para quem digitar errado
# se decisão não, break e sai do while
# print dos 3 itens

print('-'*40)
print(f'{"LOJA DO GIANEZI":^40}')
print('-'*40)

soma = qtty = barato = cont = 0
nomebarato = ''
while True:
    nome = input('Nome do Produto: ').strip()
    preço = float(input('Preço: R$ '))

    cont += 1
    soma += preço
    if preço >= 1000:
        qtty += 1

    if cont == 1 or preço < barato:
        barato = preço
        nomebarato = nome
    
    decisao = ' '
    while decisao not in 'sn':
        decisao = input('Quer continuar? [S/N] ').strip().lower()[0]

    if decisao == 'n':
        break

print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total de compras foi R$ {soma:,.2f}')
print(f'Temos {qtty} produto(s) custando mais de R$ 1,000.00')
print(f'O produto mais barato foi {nomebarato} que custa R$ {barato}')
