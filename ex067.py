# 1) DONE abre while com True para deixar infinito
# 2) DONE variavel para receber inteiro
# 3) DONE se o inteiro acima for negativo, quebrar o while 
# 4) DONE faz um for e mostra tabuada

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for i in range(1,11):
        print(f'{n} x {i} = {n*i}')
    print('-'*40)

print('Programa tabuada encerrado. Volte sempre!')
