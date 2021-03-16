# variavel para receber um angulo
# print para check
# varivael para calcular o angulo em 'radians'
# print para checar 'radians'
# print com a variavel rad e seus seno, coseeno e tangente
import math

angulo = float(input('Digite um angulo: '))
# print(angulo)
rad = math.radians(angulo)
# print(rad)
print(f'O valor do seno é: {math.sin(rad):.2f}')
print('O valor do cosseno é: {:.2f}'.format(math.cos(rad)))
print(f'O valor da tangente é: {math.tan(rad):.2f}')
