# variavel para receber nome completo DONE
# printar o nome com maiusculas DONE
# printar o nome com minusculas DONE
# variavel para receber nome dividido DONE
# printar quantas letras tem o nome completo 
# printar primeiro nome DONE

nome = input('Digite o nome completo: ').strip()
print(f'Seu nome com maiusculas é {nome.upper()}.')
print(f'Seu nome com minusculas é {nome.lower()}.')
dividido = nome.split()
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
print('Seu nome tem ao todo {} letras.'.format(len(''.join(dividido))))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(dividido[0], len(dividido[0])))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(dividido[0], nome.find(' ')))
