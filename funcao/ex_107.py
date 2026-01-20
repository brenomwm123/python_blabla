import moeda2

def linha():
    print('-='*15)

#Programa principal

preco = float(input('Informe o preço: '))

linha()
print(f'O dobro de R${preco:.2f} é {moeda2.dobro(preco):.2f}')
linha()
print(f'Metade de R${preco:.2f} é {moeda2.metade(preco):.2f}')
linha()
print(f'Aumento de 15%: {moeda2.aumentar(preco):.2f}')
linha()
print(f'Desconto de 13%: {moeda2.diminuir(preco):.2f}')
linha()
print('FIM DO PROGRAMA')

