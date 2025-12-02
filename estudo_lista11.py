from time import sleep

lista1 = []
lista2 = []

for num in range(6):
    valor = int(input('Informe um valor: '))
    lista1.append(valor)
    
print('\nPRIMEIRA LISTA PREENCHIDA.\nSOLICITANDO VALORES PARA SEGUNDA LISTA')

for num in range(6):
    valor = int(input('Informe um valor: '))
    lista2.append(valor)
    
print(f'PRIMEIRA LISTA {lista1}')
print(f'SEGUNDA LISTA {lista2}')

print('ANALISANDO QUAIS NUMEROS ESTAO PRESENTES NAS DUAS LISTAS')

lista_result = []

for num in lista1:
    if num in lista2:
       lista_result.append(num)

print(f'Os valores que estão nas duas listão são: {lista_result}') 
    