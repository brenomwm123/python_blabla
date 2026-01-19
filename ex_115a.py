from time import sleep

def menu():
        print('-'*30)
        print(f'{"MENU":^30}')
        print('-'*30)
        
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova pessoa')
        print('3 - Sair do sistema')
        print('-'*30)

while True:
    try:
        menu()
        opc = int(input('Informe sua opção: '))
        
    except ValueError:
        print('Opção invalida, informe um numero inteiro')
        continue

        
    else:
        if opc not in (1, 2, 3):
            print('Opção informada invalida\nPor favor digite 1, 2 ou 3')
            continue
        
        elif opc == 1:
            sleep(1)
            print('-'*30)
            print(f'{"VOCE SELECIONOU : Ver pessoas cadastradas":^30}')
            sleep(2)
            print('\n')

        elif opc == 2:
            sleep(1)
            print('-'*30)
            print(f'{"VOCE SELECIONOU: Cadastrar nova pessoa":^30}')
            sleep(2)
            print('\n')

        elif opc == 3:
            sleep(1)
            print('-'*30)
            print(f'{"VOCE SELECIONOU: Sair do sistema":^30}')
            sleep(2)
            print('Até mais :)')
            sleep(0.7)
            print('\n')
            break    

    