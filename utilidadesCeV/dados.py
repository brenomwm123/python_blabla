def leiaDinheiro(valor):
    valido = False
    while not valido:  
        entrada = str(input('Informe um valor: R$'))
        if entrada.isalpha():
            print('Preço invalido.')
        else:
            valido = True
            return float(entrada)
    