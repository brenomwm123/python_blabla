frase = str(input('Informe uma frase: '))
lista_palavras = frase.split()
tamanho_palavra = [len(palavra) for palavra in lista_palavras]
print(tamanho_palavra)
