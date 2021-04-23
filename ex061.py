# DONE variavel para receber primeiro termo
# DONE variavel para receber razao
# DONE variavel termo par receber primeiro termo e depois atualizar
# DONE variavel para iniciar contador
# DONE estrutura while
# DONE print de quantos número foram mostrados

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro
cont = 1
mais = 10
limite = mais

while mais != 0:
    while cont <= limite:
        print(f'{termo} ->', end=' ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais você quer? '))
    limite += mais

print('FIM!')
print(f'Progressão finalizada com {cont-1} termos mostrados!')


"""ACABEI RESOLVENDO O 62 AQUI"""
