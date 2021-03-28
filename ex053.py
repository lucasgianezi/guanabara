# DONE variavel para receber uma frase/palavra
# DONE tirar os espaços e tranformar tudo em minuscula
# DONE printar 'o inverso de x é y'
# fazer condição

frase = input('Digite uma frase: ')
frase = ''.join(frase.strip().lower().split())

print(f'O inverso de {frase} é {frase[::-1]}')

if frase == frase[::-1]:
    print('Temos um palíndromo!')
else:
    print('Não temos um palíndromo!')
    