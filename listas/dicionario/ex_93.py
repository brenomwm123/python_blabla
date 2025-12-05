##Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador['nome'] = str(input('Nome: '))
jogador['num_partidas'] = int(input('Numero de partidas: '))
jogador['gols'] = []


for i in range(jogador['num_partidas']):
    gols = input((f'Quantos gols {jogador["nome"]} fez na partida {i+1}: '))
    jogador['gols'].append(gols)

gols_tot = sum(gols)

print(jogador)
print(gols_tot)