from time import sleep
from lib.interface import *
from lib.arquivo import *

arq = 'cursoemvideo.txt'

if arquivoExiste(arq):
    

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta not in (1, 2, 3):
        print('\033[31mOpção informada invalida\033[m\nPor favor digite 1, 2 ou 3')
        continue
    elif resposta == 1:               
        cabecalho('VOCE SELECIONOU : Ver pessoas cadastradas')
        sleep(1)
    elif resposta == 2:                        
        cabecalho('"VOCE SELECIONOU: Cadastrar nova pessoa"')
        sleep(1)
    elif resposta == 3:           
        cabecalho('Saindo do sistema')
        break               