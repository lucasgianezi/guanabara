# 1) criar lista vazia OK
# 2) criar varivel (lista vazia) de posição_maior e posição_menor OK
# 3) ler 5 valores atraves de um for e guardar na lista criada
# 4) printar linha para separar OK
# 5) printar lista OK
# 6) for para fazer lista das posições do maior e menor número OK
# 7) printar maior e a lista com as posições OK
# 8) printar menor e a lista com as posições OK

# 1) criar lista vazia OK
numeros = []

# 2) criar varivel (lista vazia) de posição_maior e posição_menor OK
posi_maior=[]
posi_menor=[]

# 3) ler 5 valores atraves de um for e guardar na lista criada
for i in range(5):
    numeros.append(int(input(f'Digite um valor para a posição {i}: ')))

# 4) printar linha para separar OK
print('-='*20)

# 5) printar lista OK
print(f'Você digitou os valores: {numeros}')

# 6) for para fazer lista das posições do maior e menor número OK
for p, v in enumerate(numeros):
    if v is max(numeros):
        posi_maior.append(p)
    if v is min(numeros):
        posi_menor.append(p)

# 7) printar maior e a lista com as posições
print(f'O maior valor da lista é {max(numeros)} nas posições {posi_maior}')

# 8) printar menor e a lista com as posições
print(f'O menor valor da lista é {min(numeros)} nas posições {posi_menor}')
