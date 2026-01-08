import moeda

def linha():
    print('-='*15)

#Programa principal

preco = float(input('Informe o preço: '))

linha()
print(f'O dobro de R${preco} é {moeda.dobro(preco):.2f}')
linha()
print(f'Metade do R${preco} é {moeda.metade(preco):.2f}')
linha()
print(f'Aumento de 15%: {moeda.aumentar(preco):.2f}')
linha()
print(f'Desconto de 13%: {moeda.diminuir(preco):.2f}')
linha()
print('FIM DO PROGRAMA')