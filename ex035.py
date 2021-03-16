# DONE variavel para receber reta a
# DONE variavel para receber reta b
# DONE variavel para receber reta c
# condição

a = float(input('Comprimento reta a: '))
b = float(input('Comprimento reta b: '))
c = float(input('Comprimento reta c: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    print('É possível formar um triangulo!')
else:
    print('Não é possível formar um triangulo!')
