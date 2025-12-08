##Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, e aponte erros
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas 
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
n_pessoas = 0


while True:
    pessoa = {}
    pessoa['nome'] = str(input('Nome: '))
    
    #valida sexo
    while True:
        pessoa['sexo'] = str(input('Sexo F/M : ')).upper().strip()
        if pessoa['sexo'] in ['F', 'M']:
            break
        else:
            print('errado.')
                
    pessoa['idade'] = int(input('Idade: '))
    
    n_pessoas += 1
    pessoas.append(pessoa)
    
    #valida sim uo nao
    while True:
        resp = input('Deseja inserir outra pessoa ? S/N :').upper().strip()
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N')
    if resp == 'N': 
        break
        
print(f'Foram cadastradas {n_pessoas} pessoas.')

