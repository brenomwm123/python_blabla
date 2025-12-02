lista1 = []


while True:
    lista1.append(int(input(f'Informe um valor: ')))
    resp = int(input(f'Pressione 1 para informar outro valor e 0 para sair: '))
    if resp == 0:
        break

tamanho = len(lista1)

lista_inversa = []

for i in range(tamanho, 0, -1):
    lista_inversa.append(lista1[i-1])
    
print(lista_inversa)

