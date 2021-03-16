# co = variavel para receber cateto oposto DONE
# check para printar DONE
# ca = variavel para receber cateto adjacente DONE
# check para printar DONE
# h2 = c02 +ca2 variavel para receber hipotenis ao quadrado DONE
# check para printar h2 DONE
# h = variavel para receber h DONE 
# check para printar h DONE
# print final com texto
import math

co = float(input('Digite o cateto oposto: '))
#print(co)
ca = float(input('Digite o cateto adjacente: '))
#print(ca)
h2 = co*co + ca*ca # ou h2 = co² + ca²
# print(h2)
h = math.sqrt(h2)
# print(h)
print('A hipotenusa vale', h)
print('A hipotenusa vale', math.hypot(co, ca))
