# DONE criar variavel media_idade
# DONE criar lista vazia de homens
# DONE laço para pegar os dados de 4 pessoas
# DONE print da média de idade
# print do homem mais velho e seu nome
# quantas mulheres com menos de 20 anos


soma_idade = 0
lista_idade_homens = []
for p in range(1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')

    soma_idade += idade

print(f'\nA média de idade do grupo é {soma_idade/4} anos.')
