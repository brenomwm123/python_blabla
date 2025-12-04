#Crie um programa que leia nome, ano de nascimento, idade e carteira de trabalho e cadastre-o em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

ano_atual = datetime.now().year

pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['nascimento'] = int(input('Ano de nascimento: '))
pessoa['c_trabalho'] = str(input('Numero da carteira de trabalho, 0 caso nao tenha: '))
pessoa['idade'] = ano_atual - pessoa['nascimento']

print(pessoa['idade'])