# DONE faz tupla com lista de times
# DONE print com os 5 primeiros usando fatiamento
# DONE print com os 4 ultimos usando fatiamento
# DONE print dos times em ordem alfabetica usando sorted
# DONE print da posição da Chapecoense usando sorted + 1

times = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio', 'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR', 'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta', 'Atlético-GO')

print('-='*20)
print(f'Lista de times do Brasileirão: {times}')
print('-='*20)
print(f'Os 5 primeiros são {times[:5]}')
print('-='*20)
print(f'Os 4 últimos são {times[-4:]}')
print('-='*20)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*20)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição')
