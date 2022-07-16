class Pessoa:
    def __init__(self, nome):
        self.nome = nome


class Humano:
    def __init__(self, peso):
        self.peso = peso


class Funcionario(Pessoa, Humano):
    def __init__(self, nome, peso):
        Pessoa.__init__(self, nome)
        Humano.__init__(self, peso)


funcionario = Funcionario("John Doe", 40)

print(funcionario.nome, funcionario.peso)
