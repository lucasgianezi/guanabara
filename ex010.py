# variavel para receber o valor do dolar DONE
# variavel para receber o dinheiro em reais DONE
# imprimir quantos dolares pode comprar dividindo reais pelo valor do dolar DONE

dolar = 3.27
reais = float(input('Quantos reais voce tem? R$'))

print('Com R${:.2f} você pode comprar US${:.2f}'.format(reais, reais/dolar))
