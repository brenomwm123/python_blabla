##Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for linha in range(0, 3):
    for col in range(0, 3):
        matriz[linha][col] = int(input(f'Informe um valor para linha {linha+1} coluna {col+1}: '))

print('=-'*30)
print('MATRIZ FORMATADA:')
print('=-'*30)

for linha in range(3):
    for col in range(3):
        print(f'[{matriz[linha][col]}]', end=' ')
    print()
    
print('=-'*30)
print()