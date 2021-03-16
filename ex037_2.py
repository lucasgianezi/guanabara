# DONE variavel para receber o inteiro
# DONE criar lista vazia

inteiro = int(input('Digite um inteiro: '))
#print(inteiro)

lista = []
while inteiro > 8:
    lista.append(str(inteiro%8))
    inteiro = inteiro //8

lista.append(str(inteiro))
lista.reverse()

x = ''.join(lista)
print(x)
