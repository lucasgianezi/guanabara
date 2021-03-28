# DONE variável para receber o número inteiro
# DONE verificar se é igual ou maior que 2 para aplicar regra
# fazer condição para

num = int(input('Digite um número inteiro: '))
lista = []
if num >= 2:
    while num // 2 >= 2:
        lista.append(num%2)
        num = num // 2
    lista.append(num%2)
    lista.append(round(num//2))
    print(lista)
else:
    print(num)
