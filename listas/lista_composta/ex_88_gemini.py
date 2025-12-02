import random
import time

print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)

quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

lista_jogos = []

for i in range(quantidade_jogos):
    jogo_atual = []
    
    while len(jogo_atual) < 6:
        numero_sorteado = random.randint(1, 60)
        if numero_sorteado not in jogo_atual:
            jogo_atual.append(numero_sorteado) 
    lista_jogos.append(sorted(jogo_atual))

print('-=' * 5, f' SORTEANDO {quantidade_jogos} JOGOS ', '=-' * 5)

for indice, jogo in enumerate(lista_jogos):
    print(f'Jogo {indice + 1}: {jogo}')
    time.sleep(1) 

print('-=' * 5, '< BOA SORTE! >', '=-' * 5)
