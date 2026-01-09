import moeda

def linha():
    print('-='*15)

#Programa principal

preco = float(input('Informe o preço: '))

linha()
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
linha()
print(f'Metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
linha()
print(f'Aumento de 15%: {moeda.moeda(moeda.aumentar(preco))}')
linha()
print(f'Desconto de 13%: {moeda.moeda(moeda.diminuir(preco))}')
linha()
print('FIM DO PROGRAMA')