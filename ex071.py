# 1) DONE print layout
# 2) DONE iniciar variaveis valor (recebe inteiro do usuario), restante (inicia com valor) e ced (inicia com 50)
# 3) DONE inicia while com repetição infinita (while True)
# 4) DONE faz um if com a condição sendo: se valor restante é maior ou igual a cedula em questão. Então podemos usar no minimo 1 daquela cedula.
# 5) DONE ai ele calcula quantas cedulas podemos usar: total de cedulas = restante // ced
# 6) DONE é feito um print com a quantidade de cedulas em questao
# 7) DONE calculamos o valor restante como restante atual = restante anterior - (total de cedulas)*(valor da cedula)
# 8) DONE fazemos um if com: se restante é igual a zero, então não há nenhuma cedula mais para usar. e aí fazemos um break!
# 9) DONE tudo que foi feito entreos itens 4 e 8 está dentro do if cuja condição é de se o valor restante é maior que o valor da cedula em questão
# 10) DONE caso não seja vamos diminuir o valor da celula até que encontremos uma cedula cujo valor seja menor que o valor restante
# 11) DONE Fazemos isso colocando dentro de um else varias condições que diminuem o valor da cedula em questão para o valor imediatamente inferior
# 12) DONE ai ele sai do else, o loop acaba e ele volta para o inicio do while
# 13) DONE não é preciso colocar nada depois do ced == 1 pois quando essa condição for satisfeita, necessariamente o break será acionado
# 13) DONE print layout final

print('\n')
print('='*40)
print(F'{"BANCO DO GIANEZI":^40}')
print('='*40)

valor = int(input('Qual valor você quer sacar? R$ '))
restante = valor
ced = 50

while True:
    if restante >= ced:
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
