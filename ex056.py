# DONE criar variavel soma_idade
# DONE criar variável contagem mulheres
# DONE criar variável contagem mulheres menos 20
# DONE laço para pegar os dados de 4 pessoas
# DONE print da média de idade
# DONE print do nome do homem mais velho
# DONE PRINT mulheres com menos de 20 anos


soma_idade = 0
contagem_mulheres = 0
mulher_20 = 0
maior_idade_homem = 0

for p in range(1,5):
    print(f'----- {p}ª PESSOA -----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().lower()

    soma_idade += idade

    if sexo == 'm':
        if p == 1:
            maior_idade_homem = idade
            nome_homem = nome
        else:
            if idade > maior_idade_homem:
                nome_homem = nome
    else:
        contagem_mulheres += 1
        if idade < 20:
            mulher_20 += 1



print(f'\nA média de idade do grupo é {soma_idade/4} anos.')

if contagem_mulheres == 4:
    ('Nenhuma das pessoas é homem.')
else:
    print(f'O homem mais velho se chama {nome_homem}.')

print(f'Há {mulher_20} mulhere(s) com menos de 20 anos.')