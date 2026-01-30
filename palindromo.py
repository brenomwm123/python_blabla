def eh_palindromo(texto):
    inicio = 0
    fim = len(texto) - 1

    while inicio < fim:
        if texto[inicio] != texto[fim]:
            return False
        inicio += 1
        fim -= 1

    return True