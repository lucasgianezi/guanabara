# montar tupla com as palavras

tupla =('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in tupla:
    print(f'\nNa palavra {palavra} temos: ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
            