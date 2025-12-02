matriz = [[], [], []]

for i in range(3):
    for j in range(3):
     temp = int(input(f'Informe um valor para [{i+1},{j+1}]: '))
     matriz[i].append(temp)
     
print(matriz)   

