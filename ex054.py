# DONE importar o módulo datetime
# DONE criar contador para maior de idade
# DONE laço de repetição para ler 7 anos de nascimento
# DONE dentro do laço calcular ano atual e idade
# DONE adicionar uma condição para idades maiores que 18

from datetime import date

maior = 0

for i in range(7):
    ano = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: '))
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade >= 21:
        maior += 1

print(f'Ao todo tivemos {maior} pessoas maiores de idade.')
print(f'E também tivemos {7-maior} pessoas menores de idade.')
