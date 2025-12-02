##Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.Depois disso, mostre:
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []
cont = 0

while True:
    num = int(input('Informe um valor: '))
    lista.append(num)
    cont += 1
    
    resp = input('Deseja continuar ? S/N  ')
    
    if resp.upper() in 'Nn':
        break

print(f'Foram digitados {cont} valores')

lista.sort(reverse=True)
print(f'Valores ordenados de forma decrescente: {lista}')

if 5 in lista:
    print('Tem o numero 5 na lista.')
else:
    print('Nao tem o numero 5 na lista')
    
    