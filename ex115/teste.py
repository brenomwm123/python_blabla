from time import sleep
from lib.interface import *


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta not in (1, 2, 3):
        print('Opção informada invalida\nPor favor digite 1, 2 ou 3')
        continue
    elif resposta == 1:
        sleep(1)
        print('-'*30)
        print(f'{"VOCE SELECIONOU : Ver pessoas cadastradas":^30}')
        sleep(2)
        print('\n')
    elif resposta == 2:
            sleep(1)
            print('-'*30)
            print(f'{"VOCE SELECIONOU: Cadastrar nova pessoa":^30}')
            sleep(2)
            print('\n')
    elif resposta == 3:
            sleep(1)
            print('-'*30)
            print(f'{"VOCE SELECIONOU: Sair do sistema":^30}')
            sleep(2)
            print('Até mais :)')
            sleep(0.7)
            print('\n')
            break               