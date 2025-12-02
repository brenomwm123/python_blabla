##Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
# A) JA FOI A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma3 = maior2 = 0


for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1} e {c+1}] : '))    
        if c == 2:
           soma3 += matriz[l][c]
                
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
            
maior2 = matriz[1][0]
for i in range(0,3):
    if matriz[1][i] > maior2:
        maior2 = matriz[1][i]



print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'Soma dos pares {pares}') 
print('-='*30)
print(f'A soma dos valores da terceira coluna dá: {soma3}')
print('-='*30)
print(f'O maior valor da segunda linha foi: {maior2}')
print('-='*30)

print(f'Fim do programa')
print()
