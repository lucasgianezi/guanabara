# DONE variavel para receber reta a
# DONE variavel para receber reta b
# DONE variavel para receber reta c
# DONEcondição para verificar se as retas podem formar um triangulo
# DONE condição para verificar se é triangulo equilatero
# DONE condição para verificar se é triangulo isósceles
# DONE condição para verificar se é triangulo escaleno

a = float(input('Comprimento da reta a: '))
b = float(input('Comprimento da reta b: '))
c = float(input('Comprimento da reta c: '))

if a < (b+c) and b < (a+c) and c < (a+b):
    if a == b == c:
        forma = 'equilátero!'
    elif a == b or a == c or b == c:
        forma = 'isósceles!'
    else:
        forma = 'escaleno!'
    
    print(f'As retas podem formar um triângulo {forma}')
else:
    print("As retas não podem formar um triângulo!")

if a<(b+c) and b<(a+c) and c<(a+b):
    print('As retas podem formar um triângulo', end=' ')
    if a==b==c:
        print('equilátero!')
    elif a==b or a==c or b==c:
        print('isósceles!')
    else:
        print('escaleno!')
else:
    print('As retas não podem formar um triângulo!')