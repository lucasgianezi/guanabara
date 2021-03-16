# definir várivael para receber salario do funcionario DONE
# printar salario do funcionario DONE
# definir aumento a ser aplicado em % DONE
# printar aumento em % DONE
#printar aumento em R$ DONE
# printar salario final 

salario = int(input('Qual o salario do funcionario? '))
print('O salario do funcionario é de R${:,.2f}'.format(salario))
aumento = 0.15
print('O aumento que será dado é de {}%'.format(aumento*100))
print('O aumento em R$ será de {}.'.format(salario*aumento), end=' >>> ')
print('O novo salario será de R${}'.format(salario*(1+aumento)))