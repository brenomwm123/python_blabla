from time import sleep

def linha():
    print('=-'*20)
    
def contador_1():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    linha()
    print('Contagem de 1 até 10 de 1 em 1')
    for num in nums[1:]:
        print(num, end=' ', flush = True)
        sleep(0.4)
    print('  :p')
    linha()
    print('Contagem de 10 até 0 de 2 em 2')
    sleep(1.8)
    for num in nums[::-2]:
        print(num, end=' ', flush = True)
        sleep(0.4)
    print('  :p')
    linha()
 
#def contador_2(i, f, p):
    
       
contador_1()

print('Chegou sua vez.')
linha()
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
    
        


    