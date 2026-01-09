import moeda2

def linha():
    print('-='*15)

#Programa principal

preco = float(input('Informe o preço: '))

linha()
print(f'O dobro de {moeda2.moeda(preco)} é {(moeda2.dobro(preco,True))}')
linha()
print(f'Metade de {moeda2.moeda(preco)} é {(moeda2.metade(preco,True))}')
linha()
print(f'Aumento de 15%: {moeda2.aumentar(preco,True)}')
linha()
print(f'Desconto de 13%: {moeda2.diminuir(preco,True)}')
linha()
print('FIM DO PROGRAMA')