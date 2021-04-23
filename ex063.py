# DONE variavel para receber quantidade de termos
# DONE estabelecer variável para contagem. começa com 1
# DONE cria antecessor1 e associa a zero, que será o primeiro termo
# DONE cria o antecessor2 e associa a um, que será o segundo termo
# DONE inicia a estrutura while, enquanto cont <= n
# DONE caso seja primeiro laço, mostra antecessor1
# DONE caso seja o segundo laço, mostra antecessor2
# DONE caso seja outro laço, cria variavel atual e faz a soma de antecessor1 + antecessor2
# DONE print atual
# DONE faz o antecessor1 receber antecessor2
# DONE faz o antecessor2 receber o atual
# DONE sai do else e adiciona 1 ao cont
# DONE sai do laço while e mostra "FIM"

print('\n')
print('-'*30)
print(f'{"Sequência de Fibonacci":^30}')
print('-'*30,'\n')

n = int(input('Quantos termos você quer mostrar? '))
print('\n')

cont = 1
antecessor1 = 0
antecessor2 = 1

while cont <= n:
    if cont == 1:
        print(antecessor1, end=' -> ')

    elif cont == 2:
        print(antecessor2, end=' -> ')
    
    else:
        atual = antecessor1 + antecessor2
        print(atual, end=' -> ')

        antecessor1 = antecessor2
        antecessor2 = atual

    cont +=1

print('FIM')
print('\n')
