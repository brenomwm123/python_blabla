##Exercício Python 103: Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador,
# mesmo que algum dado não tenha sido informado corretamente.

def ficha(nome=False, gols=0):
    print(f'O jogador {nome} fez {gols} gols')
    
    
    
    
#Programa principal

print(ficha('breno', 10))