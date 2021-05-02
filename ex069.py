# DONE print layout
# DONE inicio das variaveis a, be c com zero
# DONE inicio do while com True
# DONE recebe idade 
# DONE recebe sexo e faz os ajustes
# DONE faz o while para make sure que se digitou corretamente
# DONE faz os ifs para idade maior que 18, maculino e mulher com menos de 20
# DONE dentro dos ifs coloca adiciona 1 a variavel
# DONE variavel decisão para saber se quer continuar com while
# DONE if decisão == n, break
# DONE sai do while com e encerra o programa printando as variaveis


print('-='*15)
print(f'{"CADASTRO DE PESSOAS":^30}')
print('-='*15)

a = b = c = 0

while True: 
    
    idade = int(input('Idade: '))
    
    sexo = input('Sexo [M/F]: ').strip().lower()[0]
    while sexo not in 'mf':
        sexo = input('Sexo [M/F]: ').strip().lower()[0]

    print('-'*25)

    if idade >= 18:
        a += 1
    if sexo == 'm':
        b += 1
    else:
        if idade < 20:
            c +=1

    decisao = input('Quer continuar? [S/N] ').strip().lower()[0]
    while decisao not in 'sn':
        decisao = input('Quer continuar? [S/N] ').strip().lower()[0]

    print('-'*25)
    if decisao == 'n':
        break

print('='*10, 'FIM DO PROGRAMA', '='*10)
print(f'Total de pessoas com mais de 18 anos: {a}')
print(f'Há {b} homem(ns) cadastrado(s).')
print(f'Há {c} mulher(es) com menos de 20 anos.')

