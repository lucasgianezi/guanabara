# variavel para receber a quantidade de dias DONE
# variavel para receber a quantidade de km rodados DONE
# printar para checar DONE
# preço = dias*60 + km*0.15

dias = int(input('Por quantos dias o carro foi alugado: '))
km = float(input('Quantos km foram rodados com o carro: '))
#print(dias)
#print(km)
preço = dias*60 + km*0.15
print(f'O preço a ser pago é de R${preço:.2f}')
