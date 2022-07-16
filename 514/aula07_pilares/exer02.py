class Carro:

    def __init__(self, marca, cor, velocidade):
        self.__marca = marca
        self.__cor = cor
        self.__velocidade = velocidade

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def velocide(self, velocidade):
        self.__velocidade = velocidade

    def acelerar(self):
        velocidade_atual = self.__velocidade + 10

        if velocidade_atual > 200:
            self.__velocidade = 200
        else:
            self.__velocidade += 10

    def frear(self):
        velocidade_atual = self.__velocidade - 10

        if velocidade_atual < 0:
            self.__velocidade = 0
        else:
            self.__velocidade -= 10


carro_1 = Carro("Corola", "Prata", 0)

print(carro_1.marca)

carro_1.marca = "Honda Civic"

print(carro_1.marca)

carro_1.acelerar()

carro_1.frear()
carro_1.frear()

print(carro_1.velocidade)
