##Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num = []

while True:
    temp = int(input('Informe um valor: '))
    if temp not in num:
        print(f'O numero {temp} não estava na lista, portanto foi adicionado.')
        num.append(temp)
    else:
        print(f'Como o numero {temp} ja estava na lista, nao foi adicionado.')
    resp = str(input('Deseja continuar ?? S/N  '))
    
    if resp.upper() == 'N':
        break
ordem = sorted(num)
print(f'A lista final, ordenada, com os numeros que nao se repetem ficou {ordem}')       
