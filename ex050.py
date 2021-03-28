# DONE iniciar variavel soma com valor zero 
# DONE iniciar variavel cont com valor zero 
# DONE fazer laço para obter 6 números inteiros e condição

soma = 0
cont = 0

for i in range(6):
    num = int(input('Digite un número inteiro: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'Você digitou {cont} número(s) PAR(ES) e a soma foi {soma}.')
