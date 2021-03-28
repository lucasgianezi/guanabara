# DONE variavel para receber um numero inteiro
# fazer laço de repetição

num = int(input('\nDigite um número inteiro: '))

for c in range(1,11):
    print(f'{num} x {c:^4} = {num*c:2}')
