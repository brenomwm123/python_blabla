from utilidadesCeV import moeda
from utilidadesCeV import dados

def linha():
    print('-='*15)

#Programa principal

preco = dados.leiaDinheiro('canto')
moeda.amostrar(preco, 90, 5)