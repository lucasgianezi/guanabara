# DONE variável para receber o número inteiro
# converter para binário

inteiro = int(input('Digite um número inteiro: '))
#print(inteiro)
lista = []
while inteiro >= 2:
    lista.append(str(inteiro%2))
    inteiro = inteiro//2

lista.append(str(inteiro))
lista.reverse()
x = ''.join(lista)
print(x)
