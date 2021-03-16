#variavel para receber numero inteiro DONE
#mostra o proprio numero DONE
#mostra ele x 2 DONE
#mostra ele x 3 DONE

num = int(input('\nDigite um inteiro: '))
print('\nA tabuada do {} é:'.format(num))
print('-'*12)
for i in range(1,11):
    print("{} x {:2} = {:2}".format(num, i, num*i))
print('-'*12)
