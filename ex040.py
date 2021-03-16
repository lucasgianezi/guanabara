# variavel para receber a primeira nota
# variavel para receber a segunda nota
# variavel para receber a media
# condição

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2
# print(n1, n2, media)

if media < 5:
    print('Reprovado')
elif 5 <= media < 7:
    print('Recuperação')
else:
    print('Aprovado')