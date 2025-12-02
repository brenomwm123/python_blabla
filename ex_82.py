##Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista_mae = []
lista_p = []
lista_i = []

while True:
    num = int(input('Informe um valor: '))
    lista_mae.append(num)

    if num % 2 == 0:
        lista_p.append(num)
    else:
        lista_i.append(num)
    
    resp = input('Deseja continuar ? S/N  ')
    
    if resp.upper() in 'Nn':
        break
    
print(f'\nLista completa: {lista_mae}')
print(f'Lista de pares: {lista_p}')
print(f'Lista de impares: {lista_i}\n')


