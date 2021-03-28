# DONE variavel para receber um número inteiro
# DONE abrir contador
# fazer o laço de repetição for

num = int(input('\nDigite um número inteiro: '))
cont = 0

for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print(c, end=' ')

print(f'\nO número {num} foi divisível {cont} vez(es).')

if cont != 2:
    print('Portanto, ele não é primo!')
else:
    print('Portanto, ele é primo!')
    