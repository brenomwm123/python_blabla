##Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome=False, gols=0):
    print()
    if nome.strip():
        print(f'O jogador {nome} fez {gols} gols')
    else:
        print(f'O jogador <desconhecido> fez {gols} gols')
    print()
    
    
#Programa principal
nome = input('Nome do jogador: ')
gols = input('Quantos gols: ')

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)