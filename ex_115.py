from time import sleep

while True:
    try:
        print('-'*30)
        print(f'{"MENU":^30}')
        print('-'*30)
        
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova pessoa')
        print('3 - Sair do sistema')
        print('-'*30)
        
        opc = int(input('Informe sua opção: '))
        
    except:
        print('ERRADO')
        print('-'*30)
        continue
    else:
        if opc == 1:
            sleep(1)
            print('-'*30)
            print(f'{"VOCE SELECIONOU : Ver pessoas cadastradas":^30}')
            sleep(2)
            print('\n')

        if opc == 2:
            sleep(1)
            print('-'*30)
            print(f'{"VOCE SELECIONOU: Cadastrar nova pessoa":^30}')
            sleep(2)
            print('\n')

        if opc == 3:
            sleep(1)
            print('-'*30)
            print(f'{"VOCE SELECIONOU: Sair do sistema":^30}')
            sleep(2)
            print('\n')
            break    

    