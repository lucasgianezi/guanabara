# variavel para receber um número real DONE
# check para printar o numero DONE
# variavel para obter parte inteira DONE
# printar parte fracionaria DONE
# variavel para obter parte fracionaria
# printar parte fracionaria

import math

num = float(input('Digite um número real: '))
print(num)
inteira_2 = math.trunc(num)
inteira = int(num//1)
inteira_3 = int(num)
print(f'A parte inteira é {inteira}')
print(f'A parte inteira é {inteira_2}')
print(f'A parte inteira é {inteira_3}')
