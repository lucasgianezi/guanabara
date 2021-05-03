

print('\n')
print('='*40)
print(F'{"BANCO DO GIANEZI":^40}')
print('='*40)

valor = int(input('Qual valor você quer sacar? R$ '))
restante = valor
ced = 50

while True:
    if restante // ced >= 1:
        totced = restante//ced
        print(f'Total de {totced} cédulas de R${ced},00.')
        restante -= totced * ced
        if restante == 0:
            break
    else:
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

print('='*40)
print('Volte sempre ao BANCO GIANEZI! Tenha um bom dia!')
