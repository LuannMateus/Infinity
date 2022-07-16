class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario


class Estagiario(Funcionario):
    def __init__(self, matricula, nome, salario):
        super().__init__(matricula, nome, salario)


class Gerente(Funcionario):
    def __int__(self, matricula, nome, salario):
        super().__init__(matricula, nome, salario)


e = Estagiario("123", "John Doe", 2000)

s = Gerente("423123", "Mary Doe", 100000)

print(e.nome)

print(s.nome)
