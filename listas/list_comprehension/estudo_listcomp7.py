numeros = list(range(1, 51))

primos = [
    num for num in numeros
    if num > 1 and all(num % i != 0 for i in range(2, num))
]

print(primos)