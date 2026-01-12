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
    
    print(f'{"Preço analisado:":<20} {moeda(preco):<8}')
    print(f'{"Dobro do preço:":<20} {moeda(dobro(preco)):<8}')
    print(f'{"Metade do preço:":<20} {moeda(metade(preco)):<8}')
    print(f'{f"{aumento}% de aumento:":<20} {moeda(preco + (preco * porcentagem_aumento)):<8}')
    print(f'{f"{desconto}% de desconto:":<20} {moeda(preco - (preco * porcentagem_desconto)):<8}')
    print('-'*30)
    
    