# DONE importar biblioteca random
# DONE fazer tupla com 5 elementos e um randint em cada um destes 5 elementos
# printar os valores lado alado sem os parenteses das tuplas
# printar maior usando max
# printar menor usando min

from random import randint as rd

valores = (rd(1,10),rd(1,10),rd(1,10),rd(1,10),rd(1,10))

print('Os valores sorteados foram:', end=' ')
for i in valores:
    print(i, end=' ')
print(f'\nO maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
