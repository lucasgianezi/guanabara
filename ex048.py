# DONE definir a soma igual a zero
# DONE gerar valores entre 1 e 500
# DONE mostrar os impares e descartar o resto
# DONE dentre estes mostrar os que são multiplo de 3

soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3 == 0:
        print(c)
        cont += 1
        soma += c
print(f'A soma de todos os valores solicitados é {soma}.')
print(f'Há {cont} números que satisfazem essa condição.')
