'''
# DONE gerar lista com todos os número entre 1 e 50
# colocar condição para saber se o número é par

for c in range(1,51):
    if c % 2 == 0:
        print(c, 'PAR')


# DONE colocar lista vazia
# DONE mostrar todo os números de 1 até 50
# DONE fazer condição
# DONE adicionar a lista os numeros pares se a condição for satisfeita
# DONE print lista

lista = []
for c in range(1,51):
    if c % 2 == 0:
        lista.append(c)

print(lista, 'Acabou')
'''

# DONE gerar lista até 50
# DONE fazer condição dentro da lista
# DONE se a condição for satisfeita printar

for c in range(1, 51):
    if c % 2 == 0:
        print(c, end=' ')
print('Acabou')
