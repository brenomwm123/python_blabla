#Crie um programa que leia nome, ano de nascimento, idade e carteira de trabalho e cadastre-o em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

ano_atual = datetime.now().year

pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['idade'] = ano_atual - pessoa['nascimento']

pessoa['c_trabalho'] = int(input('Numero da carteira de trabalho (0 caso nao tenha): '))
if pessoa['c_trabalho'] != 0:
    pessoa['ano_contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salario: '))
    pessoa['aposentadoria'] = pessoa['ano_contratacao'] - pessoa['nascimento'] + 35
    print(f'Vai se aposentar daqui {pessoa["aposentadoria"]} anos')