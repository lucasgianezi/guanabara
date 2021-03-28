# DONE print layout inicio
# DONE variavel para receber primeiro termo
# DONE variavel para receber razao
# DONE fazer o laço com 10 repetições

print('='*30)
print(f'{"10 TERMOS DE UMA PA":^30}')
print('='*30)

termo = int(input('Qual o primeiro termo: '))
razao = int(input('Qual a razão: '))

for i in range(10):
    print(f'{termo}', end=' -> ')
    termo += razao
print('ACABOU')
