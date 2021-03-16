

n = input('Digite algo: ')
print('O tipo primitivo do que vc digitou é {}'.format(type(n)))
print('É somente espaços?', n.isspace())
print('É somente numero?', n.isnumeric())
print('É somente letras?', n.isalpha())
print('É somente numero ou alfa ou os dois?', n.isalnum())
print('As letras que tem são somente maiusculas?', n.isupper())
print('As letras que tem são somente minusculas?', n.islower())
print('As letras que tem são capitalizadas? {}'.format(n.istitle()))