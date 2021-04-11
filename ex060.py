# DONE variável para receber o número
# DONE criar variavel total
# DONE criar laço

num = int(input('\nDigite um número para calcular seu fatorial: '))

total = 1

print(f'Calculando o fatorial de {num}! = {num}', end=' ')

while num > 1:
    total *= num
    num -= 1
    print('x', num, end=' ')

print('=', total)
