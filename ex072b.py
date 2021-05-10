# DONE fazer a tupla com os números por extenso
# DONE iniciar o while true infinito
# DONE recebe entrada o usuario com condição while para satisfazer condição
# DONE print do numero por extenso
# DONE recebe entrada do usuario com while para condição para parar
# DONE break se condição é n 
# DONE fazer o print com a tupla

extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = ''
    while num not in range(0,21):
        num = int(input('Digite um número entre 0 e 20: '))
    
    print(f'Você digitou o número {extenso[num]}')

    condição = ' '
    while condição not in 'sn':
        condição = input('Você quer continuar? [S/N] ').strip().lower()[0]
    if condição == 'n':
        break

print('Obrigado. Volte sempre!')
