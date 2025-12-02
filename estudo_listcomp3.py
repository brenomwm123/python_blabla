lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

lista_result = [ num**2 for num in lista_original if num % 2 == 0 ]

print(lista_result)

