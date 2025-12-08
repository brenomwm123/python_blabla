##Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, e aponte erros
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas 
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

pessoas = []
mulheres = []
soma = mdia = 0

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
    soma += pessoa['idade']
    
    pessoas.append(pessoa)
    
    #valida sim uo nao
    while True:
        resp = input('Deseja inserir outra pessoa ? S/N :').upper().strip()
        if resp in 'SN':
            break
        print('ERRO! responda apenas S ou N')
    if resp == 'N': 
        break
    
media = soma / len(pessoas)

print('-='*20)       
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print('-='*20)     
print(f'A media da idade das pessoas foi de {media} anos.')
print('-='*20)     
print('As mulheres cadastradas foram : ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('-='*20)
print('Pessoas mais velhas que a media:: ', end='')
for p in pessoas:
    if p['idade'] > media:
        print(f'{p["nome"]}', end ='')