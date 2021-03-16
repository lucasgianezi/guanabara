#criar variavel para receber numero DONE
#mostrar o dobro DONE
#mostarr o triplo DONE
#mostrar a raiz quadrada DONE

import math

num = float(input('Digite um numero: '))
print('O seu dobro é: {}. \nO seu triplo é: {}.'.format(num*2, num*3))
print('A sua raiz quadrada é: {}'.format(math.sqrt(num)))
print('A sua raiz quadrada é: {}'.format(pow(num, 1/2)))
print('A sua raiz quadrada é: {}'.format(pow(num, 0.5)))
print('A sua raiz quadrada é: {}'.format(num**0.5))
print('A sua raiz quadrada é: {}'.format(num**(1/2)))