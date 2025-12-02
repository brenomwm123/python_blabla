frase = str(input('Informe uma frase : '))
lista_palavras = frase.split()

lista_final = [palavra for palavra in lista_palavras if palavra[-1] == 'o']
print(lista_final)