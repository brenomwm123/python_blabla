##Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      
# guardando tudo em uma lista. No final, mostre:                                                                                                    
# A) Quantas pessoas foram cadastradas.                                                                                                                
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
resp = 0
mai = men = 0


while True:
    dados.append(str(input('Informe seu nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        elif dados[1] < men:
            men = dados[1]    
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar ? [S/N]  \n')
    if resp in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi {mai}, peso de: ', end='')
for p in pessoas:
    if p[1] == mai:
        print(f'{p[0]}',end=', ')
print(f'O menor peso foi {men}, peso de: ', end='')
for p in pessoas:
    if p[1] == men:
        print(f'{p[0]}',end=', ')
    