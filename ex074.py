# importar biblioteca random
# gerar tupla aleatoria

from random import randint as rt

numeros = (rt(0,30), rt(0,30), rt(0,30), rt(0,30), rt(0,30))
print(f'Os números gerados são: {numeros}')
print(f'O maior valor gerado foi {max(numeros)}')
print(f'O menor valor gerado foi {min(numeros)}')
