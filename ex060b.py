# DONE variavel para receber número

n = int(input('Digite um número para calcular o seu fatorial: '))
total = n

print(f'Calculando o fatorial de {n}! = {n}', end=' ')

for c in range(n-1, 0, -1):
    total *= c
    print('x', c, end=' ')


print('=', total)
