# variavel para receber input com a letra do sex da pessoa

s = input('Informe seu sexo [M/F]: ').strip().upper()[0]

while s not in 'MF':
    s = input('Dados inválidos. Informe seu sexo [M/F]: ').strip().upper()[0]

print(f'Sexo {s} registrado com sucesso!')
