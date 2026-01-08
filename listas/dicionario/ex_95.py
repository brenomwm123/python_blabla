jogadores = []

while True:
    jogador = {}
    jogador['nome'] = input('Nome: ')
    jogador['partidas'] = int(input('Número de partidas: '))
    jogador['gols'] = []

    for i in range(jogador['partidas']):
        gols = int(input(f'Quantos gols {jogador["nome"]} fez na partida {i+1}? '))
        jogador['gols'].append(gols)

    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador)

    resp = input('Deseja inserir outro jogador? [S/N] ').upper().strip()
    if resp == 'N':
        break

print('-='*25)
print(f'{"cod":<4}{"nome":<15}{"gols":<20}{"total":>5}')
print('-' * 50)

for i, j in enumerate(jogadores):
    gols_str = ', '.join(map(str, j["gols"]))
    print(f'{i:<4}{j["nome"]:<15}{gols_str:<20}{j["total"]:>5}')

while True:
    print('-' * 50)
    cod = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if cod == 999:
        print('Encerrado.')
        break
    if cod >= len(jogadores):
        print('Código inválido! Tente novamente.')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[cod]["nome"]}:')
        for i, g in enumerate(jogadores[cod]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
