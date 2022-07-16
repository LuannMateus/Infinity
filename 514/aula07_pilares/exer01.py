class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.__nome = nome
        self.__idade = idade
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        self.__idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf


p = Pessoa("John Doe", 40, "0000000000000000")

print(p.nome)

p.nome = "Mary Doe"

print(p.nome)
