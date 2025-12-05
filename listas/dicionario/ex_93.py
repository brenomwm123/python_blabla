##Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador['nome'] = str(input('Nome: '))
jogador['partidas'] = int(input('Numero de partidas: '))
jogador['gols'] = []


for i in range(jogador['partidas']):
    gols = int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}: '))
    jogador['gols'].append(gols)

gols_tot = sum(jogador['gols'])

print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')

print('-='*20)

for i in range(jogador['partidas']):
    print(f'Na partida {i+1}, {jogador["nome"]} marcou {jogador["gols"][i]} gols.')
print('-='*20)

print(f'Total de gols: {gols_tot}')