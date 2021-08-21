numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

numero = int(input('Digite um número entre 0 e 20: '))
while 0 > numero or numero > 20:
    numero = int(input('Tente novamente. Digite um número entre 0 e 20: '))

print(f'Você digitou o número {numeros[numero]}')
