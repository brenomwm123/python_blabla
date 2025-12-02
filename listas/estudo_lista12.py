lista1 = [1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 7, 7, 8, 9, 9, 9]

lista_result = []

for num in lista1:
    if num not in lista_result:
        lista_result.append(num)
    
print(lista_result)
        