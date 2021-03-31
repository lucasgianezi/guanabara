# criar lista vazia
# fazer laço de repetição para pegar o peso de 5 pessoas
# colocar os pesos na lista
# pegar o maior e o menor

lista = []
for i in range(5):
    peso = float(input(f'Qual o peso da {i+1}ª pessoa? '))
    lista.append(peso)

print(f'O menor peso é {min(lista)}.')
print(f'O maior peso é {max(lista)}.')
