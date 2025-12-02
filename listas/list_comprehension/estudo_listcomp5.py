numeros = list(range(1, 31))

impares_cubos = [num**3 for num in numeros if num % 2 != 0]

print(impares_cubos)