# cria variavel soma e cont
# cria laço while com a leitura de n dentro
# cria condição if com break dentro


soma = cont = 0

while True:
    n = int(input('Digite um inteiro [999 para parar]: '))
    if n == 999:
        break
    soma += n
    cont += 1

print(f'A soma dos {cont} valores foi {soma}!')
