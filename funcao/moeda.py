def aumentar(valor):
    a = valor * 1.15
    return a

def diminuir(valor):
    d = valor * 0.87
    return d

def dobro(valor):
    d = valor * 2
    return d

def metade(valor):
    m = valor / 2
    return m

def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')