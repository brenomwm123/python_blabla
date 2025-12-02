frase = str(input('Informe uma frase: '))
lista_palavras = frase.split()

lista_resposta = [palavra for palavra in lista_palavras if len(palavra) > 5]

print(lista_resposta)

