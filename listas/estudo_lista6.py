numeros = []

for i in range(5):
    valor = int(input(f'Digite o valor do {i+1} numero: '))
    numeros.append(valor)
    
print(f'Maior numero: {max(numeros)}')
print(f'menor numero: {min(numeros)}')