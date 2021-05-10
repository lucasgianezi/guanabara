# DONE fazer a tupla com os números por extenso
# DONE fazer a entrada do usuario com while infinito para garantir a condição
# DONE fazer o print com a tupla

extenso = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num in range(0,21):
        break
    print('Tente novamente. ', end='')

print(f'Você digitou o número {extenso[num]}.')
