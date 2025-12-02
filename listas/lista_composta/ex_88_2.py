##Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites
# .O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo
# , cadastrando tudo em uma lista composta.

from random import randint
import time

print('-=-'*15)
print(f'{"GERADOR DE PALPITES MEGA SENA":^45}')
print('-=-'*15)

#qtd = int(input('Quantos jogos vc quer sorteados: '))

jogo = []


for c in range(0,6):
    num_sorteado = randint(1,60)
    if num_sorteado not in jogo:
        jogo.append(num_sorteado)
        
jogo_certo = sorted(jogo)
print(jogo) 
