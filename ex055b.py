# criar variaveis maior e menor com valor zero
# laço para ler o peso de 5 pessoas
# 

maior = 0
menor = 0

for pess in range(1,6):
    peso = float(input(f'Digite o peso da {pess}ª pessoa: '))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior}kg.')
print(f'O menor peso lido foi de {menor}kg.')

