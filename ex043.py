# DONE variavel para receber o peso de uma pessoa
# DONE variavel para receber a altura de uma pessoa
# DONE variavel para calcular o IMC
# fazer as condições

peso = float(input('Qual o peso? '))
altura = float(input('Qual a altura? '))
#print(peso, altura)
imc = peso / (altura**2)
print('O IMC desta pessoa é', round(imc,1))

print('Esta pessoa está', end=' ')
if imc < 18.5:
    print('abaixo do peso!')
elif imc < 25:
    print('no peso ideal!')
elif imc<30:
    print('com sobrepeso!')
elif imc<40:
    print('com obesidade!')
else:
    print('com obesidade mórbida!')