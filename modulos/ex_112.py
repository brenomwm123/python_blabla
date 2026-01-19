from utilidadesCeV import moeda
from utilidadesCeV import dados

def linha():
    print('-='*15)

#Programa principal

preco = dados.leiaDinheiro()
moeda.amostrar(preco, 90, 5)