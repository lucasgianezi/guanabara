# 1) criar lista vazia para armazenar os valores OK
# 2) criar um while True com as condições dentro OK
# 3) colocar em ordem crescente OK
# 4) printar a lista OK



# 1) criar lista vazia para armazenar os valores OK
valores = []

# 2) criar um while True com as condições dentro OK
while True:
    x = int(input(f'Digite um valor: '))
    if x not in valores:
        valores.append(x)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar')

    y = input('Quer continuar? [S/N] ')
    if y.strip().lower() == 'n':
        break

print('-='*30)

# 3) colocar em ordem crescente OK
valores.sort()

# 4) printar a lista OK
print(f'Você digitou os valores {valores}')
