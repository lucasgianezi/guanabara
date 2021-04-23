# DONE criar uma variavel para receber o primeiro número inteiro
# DONE inciar contador cont
# DONE iniciar soma
# DONE fazer a estrutura while
# DONE dentro do while somar 1 ao contador e somar n a soma
# DONE colocar o input dentro do while de novo
# DONE print fim fora do while do contador e da soma


n = int(input('Digite um número inteiro [999 para parar]: '))
cont = 0
soma = 0

while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número inteiro [999 para parar]: '))

print(f'Foram digitados {cont} número(s).')
print(f'A soma deles é {soma}')
