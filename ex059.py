# DONE variavel para receber primeiro numero
# DONE variavel para receber segundo numero
# DONE print do menu e entrada de dados
# DONE fazer laço de repetição
# DONE colocar as condições dentro do laço
# DONE fazer novo input ao final do laço
# DONE print de mensagem de saída

num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

x = int(input("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa

>>>> Qual sua opção? """))

while x != 5:
    if x == 1:
        print(f'\nA soma de {num1} e {num2} é {num1+num2}.')
    elif x == 2:
        print(f'\nA multiplicação de {num1} e {num2} é {num1*num2}.')
    elif x == 3:
        if num1 == num2:
            print('\nOs números são iguais!')
        else:
            print(f'\nO maior valor entre {num1} e {num2} é {max(num1, num2)}.')
    elif x == 4:
        num1 = int(input('\nDigite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

    else:
        print('Opção inválida. Tente novamente!')

    x = int(input("""
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa

>>>> Qual sua opção? """))

print('\nObrigado!\nAté a próxima!\n')
