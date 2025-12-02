frase = input('Informe uma frase : ')
lista_frase = frase.split()

com_a = [palavra for palavra in lista_frase if palavra.upper().startswith('A')]
print(com_a)
