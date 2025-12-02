##Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.                                                                                                                
# C) O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_pares = 0
qtd_pares = 0

soma_3coluna = 0
maior_2linha = 0

#preenche a matriz
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l+1}] e [{c+1}] : '))
        
        #soma valores da terceira coluna
        if c == 2:
            soma_3coluna += matriz[l][c]   
        
        #confere se é a primeira ocasião
        if l == 1 and c == 0:
            maior_2linha = matriz[l][c]
            
        #caso seja, compara se é maior que o maior termo
        else:
            if matriz[l][c] > maior_2linha and l == 1:
                maior_2linha = matriz[l][c]
                
        #Conta a quantidade de numeros pares na matriz e os soma
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
            qtd_pares += 1
        


print('-='*30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
    
print('-='*30)  

if qtd_pares != 0:
    print(f'Voce digitou {qtd_pares} valores pares que somam {soma_pares}')
else:
    print('Nenhum valor par informado')

print('-='*30)

print(f'A soma da terceira coluna foi {soma_3coluna}')

print('-='*30)

print(f'O maior valor da segunda linha foi {maior_2linha}')

print('-='*30)
     