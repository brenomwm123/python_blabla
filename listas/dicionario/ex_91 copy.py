##Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

dados = {f'jogador {i}': randint(1,6) for i in range(1,5)}

print('-='*20)
print('Jogando os dados ...')
print('-='*20)

sleep(1.5)

for k,v in dados.items():
    print(f'O {k} tirou o numero {v}')

print('-='*20)

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)

for i,v in enumerate(ranking):
    print(f'{i+1} LUGAR: {v[0]}, dado de numero {v[1]}')
    
print('-='*20)