class Pessoa:
    nome = None
    idade = None

    def __init__(self, n, i):
        self.nome = n
        self.idade = i

    def printNome(self):
        print(self.nome)

    def printIdade(self):
        print(self.idade)

    def setIdade(self, num):
        self.idade = num

    def setNome(self, nome):
        self.nome = nome


#eu = Pessoa()
# eu.setNome("Augusto")
# eu.setIdade(25)

eu = Pessoa("augusto", 25)
eu.printNome()
eu.printIdade()
