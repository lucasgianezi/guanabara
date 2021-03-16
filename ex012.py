# variavel para receber o preço do produto DONE
# definir desconto DONE
# printar desconto em % DONE
# printar desconto em $ DONE
# printar novo preço DONE

price = float(input('Qual o preço do produto? '))
desconto = 5
print('O desconto que será dado é de {}%'.format(desconto))
print('Portanto, o desconto em reais será de R${}. E o novo preço com desconto é de R${}'.format(price*desconto/100, price*(1-desconto/100)))
