# DONE cria soma, cont, media, maior e menor
# DONE associa continuar a sim
# DONE entra no while se coninuar é igual a sim
# DONE recebe número inteiro
# DONE cria variavel de controle
# DONE faz soma
# DONE faz cont
# DONE faz se cont == 1 e faz o menor e o maior receberem n
# DONE else: if n maior que maior, maior recebe n
# if n menor que menor, menor recebe n
# DONE fora do while print cont, média, maior e menor

soma = cont = media = menor = maior = 0
continuar ='s'

while continuar == 's':
    n = int(input('Digite um número inteiro: '))
    continuar = input("Quer coninuar? [s/n] ")
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'Você digitou {cont} números.')
print(f'A média é {soma/cont}.')
print(f'O maior valor é {maior}.')
print(f'O menor valor é {menor}.')