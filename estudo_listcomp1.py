# [expressao for item in lista if condicao]
#Exercício 1
#Dada uma lista de números, crie uma nova lista contendo apenas os números maiores que 10, usando list comprehension.

lista1 = []

while True:
    lista1.append(int(input('Informe um valor inteiro: ')))
    resp = int(input('Deseja continuar ? 1:SIM  0:NAO  '))
    if resp == 0:
        break

maiores10 = [num for num in lista1 if num > 10]
print(f'Os numeros informados maiores que 10 foram: {maiores10}')