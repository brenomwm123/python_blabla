def leiaDinheiro():
    valido = False
    while not valido:  
        entrada = str(input('Informe um valor: R$')).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print('Preço invalido.')
        else:
            valido = True
            return float(entrada)
    