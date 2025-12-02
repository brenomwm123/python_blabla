from random import randint

numeros = []

for i in range(10):
    numeros.append(randint(1,100))
    
numeros.sort()
print(numeros)

print(f'O maior numero é: {max(numeros)}')
print(f'O menor numero é: {min(numeros)}')
print(f'Soma dos valores: {sum(numeros)}')
print(f'Tamanho da lista: {len(numeros)}')
print(f'Media dos valores da lista:', sum(numeros)/len(numeros))
