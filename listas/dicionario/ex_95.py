##Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


jogadores = []

while True:
    jogador = {}
    jogador['nome'] = str(input('Nome: '))
    jogador['partidas'] = int(input('Numero de partidas: '))
    jogador['gols'] = []


    for i in range(jogador['partidas']):
        gols = int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}: '))
        jogador['gols'].append(gols)

    gols_tot = sum(jogador['gols'])
    jogadores.append(jogador)
    resp = input('Deseja inserir outro jogador ? S/N  ').upper().strip()
    if resp == 'N':
        break

print('-='*25)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":>5}')
print('-' * 50)
for i, j in enumerate(jogadores):
    print(f'{i:<4}{j["nome"]:<15}{str(j["gols"]):<20}{sum(j["gols"]):>5}')
# print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas')

# print('-='*20)

# for i in range(jogador['partidas']):
#     print(f'Na partida {i+1}, {jogador["nome"]} marcou {jogador["gols"][i]} gols.')
# print('-='*20)

# print(f'Total de gols: {gols_tot}')