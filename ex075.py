# inserção dos números por entrada do usuario OK
# fazer tupla com os números OK
# print da tupla OK
# quantas vezes o valor 9 apareceu OK
# qual a posição do primeiro valor 3 OK
# há valores pares digitados. Se sim, qual? OK

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

numeros = (a, b, c, d)
print(f'Você digitou os valores {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vez(es)')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')

print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
    