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