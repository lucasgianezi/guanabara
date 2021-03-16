# variavel para receber a largura da parede DONE
# variavel para receber a altura da parede DONE
# variavel que define a area da parede DONE
# definir eficiencia
# printar a area da parede
# printar eficiencia
# printar area/eficiencia


largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = altura*largura
eficiencia = 2
print('A area da parede é de {} m²'.format(area))
print('Cada litro de tinta pinta {} m²'.format(eficiencia))
print('São necessários {} litros de tinta'.format(area/eficiencia))