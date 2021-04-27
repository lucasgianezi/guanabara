# 1) variavel para receber inteiro
# 2) mostra tabuada
# 3) colocar itens 1 e 2 dentro de um while


while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
    print('-'*40)

print('Programa tabuada encerrado. Volte sempre!')
