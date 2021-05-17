# DONE importar biblioteca random para sortear valores
# DONE fazer uma tupla vazia
# DONE fazer um for in range para 5 repeticoes
# DONE em cada repetição sortear um valor, colocá-lo em uma tupla e depois concatenar com a tupla inicial
# DONE printar tupla inicial
# DONE printar maior valor
# DONE printar menor valor


from random import randint as rd

a = ()

for i in range(1,6):
    b = (rd(1,10),)
    a += b

print(f'Os valores sorteados foram: {a}')
print(f'O maior valor sorteado foi {max(a)}')
print(f'O menor valor sorteado foi {min(a)}')
