# DONE variavel para receber a distancia da viagem
# DONE print para check
# DONE fazer a condição para distancia menor ou igual a 200km
# DONE print para check
# fazer a condição para distancia maior que 200km
# print para check

distancia = float(input('Qual a distancia da viagem? '))
#print(distancia)

if distancia <= 200:
    print(f'O preço será R${distancia*0.5:.2f}')
else:
    print('O preço será R${:.2f}'.format(distancia*0.45))

print(f'O preço será R${distancia*0.5:.2f}') if distancia <= 200 else print('O preço será de R${:.2f}'.format(distancia*0.45))
