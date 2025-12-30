##Exercício Python 101: Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

from datetime import datetime

def voto(ano=0):
    dif_ano = ano_atual - ano
    if dif_ano < 16:
        return 'VOTO NEGADO'
    elif dif_ano < 18:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO OBRIGATÓRIO'
    

ano_atual = datetime.now().year
ano_nasc = int(input('Informe seu ano de nascimento: '))

print(voto(ano_nasc))
