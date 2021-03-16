n1 = int(input('Qual o primeiro valor? '))
n2 = int(input('Qual o outro valor? '))
print('A soma é {}\no produto é {}, a divisão é {:.3f}'.format(n1+n2, n1*n2, n1/n2), end=" >>> ")
print('Divisão inteira é {}, resto divisao é {}, a potencia é {}'.format(n1//n2, n1%n2, n1**n2))