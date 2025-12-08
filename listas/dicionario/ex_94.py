##Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, e aponte erros
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas 
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = {}
n_pessoas = 0

while True:
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo F/M : '))
    pessoas['idade'] = int(input('Idade: '))
    n_pessoas += 1
    resp = input('Deseja inserir outra pessoa ? S/N :')
    if resp in 'Nn':
        break
    
print(pessoas)