#
#


lista = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)

print('-'*60)
print(f'{"Listagem de Preços":^60}')
print('-'*60)

for n in lista:
    if lista.index(n) % 2 == 0:
        print(f'{n:.<50}R$', end='')
    else:
        print(f'{n:>7.2f}')

print('-'*60)
