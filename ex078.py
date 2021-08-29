# 1) criar lista vazia OK
# 2) ler 5 valores atraves de um for e guardar na lista criada OK
# 3) printar linha para separar OK
# 4) printar lista OK
# 5) criar variavel 'maximo' e 'minimo' OK
# 6) printar maior valor e seus respectivos indices OK
# 7) printar menor valor e seus respectivos indices OK


# 1) criar lista vazia OK
numeros = []

# 2) ler 5 valores atraves de um for e guardar na lista criada OK
for i in range(5):
    numeros.append(int(input(f'Digite um valor para a posição {i}: ')))

# 3) printar linha para separar OK
print('-='*20)

# 4) printar lista OK
print(f'Você digitou os valores {numeros}')

# 5) criar variavel 'maximo' e 'minimo' OK
maximo = max(numeros)
minimo = min(numeros)

# 6) printar maior valor e seus respectivos indices OK
print(f'O maior valor digitado foi {maximo} nas posições ', end='')
for c, numero in enumerate(numeros):
    if numero is maximo:
        print(f'{c}...', end='')

# 7) printar menor valor e seus respectivos indices OK
print(f'\nO menor valor digitado foi {minimo} nas posições ', end='')
for c, numero in enumerate(numeros):
    if numero is minimo:
        print(f'{c}...', end='')
