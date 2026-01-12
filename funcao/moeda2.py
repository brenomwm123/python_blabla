def aumentar(valor,formato=False):
    a = valor * 1.15
    return a if formato==False else moeda(a)


def diminuir(valor,formato=False):
    d = valor * 0.87
    return d if formato==False else moeda(d)

def dobro(valor,formato=False):
    d = valor * 2
    return d if formato==False else moeda(d)

def metade(valor,formato=False):
    m = valor / 2
    return m if formato==False else moeda(m)

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

def amostrar(preco=0, aumento=10, desconto=5):
    porcentagem_aumento = aumento / 100
    porcentagem_desconto = desconto / 100
    
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    
    print(f'Preço analisado: {moeda(preco)}')
    print(f'Dobro do preço: {moeda(dobro(preco))}')
    print(f'Metade do preço: {moeda(metade(preco))}')
    print(f'{aumento}% de aumento: {moeda(preco + (preco * porcentagem_aumento))}')
    print(f'{desconto}% de desconto: {moeda(preco - (preco * porcentagem_desconto))}')
    
    