#Declaração de clase
class Gafanhoto:
    def __init__(self): #Metodo construtor
        #Atributos de instancia
        self.nome = ""
        self.idade = 0        
    #Metodos de instancia
    def aniversario(self):
        self.idade = self.idade + 1
    def mensagem(self):
        return f'{self.nome} é Gafanhoto e tem {self.idade} anos de idade.'
#Declaração de objetos
g1 = Gafanhoto()
g1.nome = 'Breno'
g1.idade = 22
g1.aniversario()

g2 = Gafanhoto()
g2.nome = 'Mylenna'
g2.idade = 25

print(g1.mensagem())
print(g2.mensagem())