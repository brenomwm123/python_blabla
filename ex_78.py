##Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
maior = menor = 0

for i in range (0, 5):
    num = int(input(f'Informe o valor para a posição {i+1}: '))
    valores.append(num)
    if i == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
            
print(f'O maior valor foi {maior} nas posiçoes', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}..', end=' ')
        
      
print(f'\nO menor valor foi {menor} nas posiçoes', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}..', end=' ')
        