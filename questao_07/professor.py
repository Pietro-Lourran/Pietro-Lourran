# Classe Professor e Pessoa e salário
class Professor(Pessoa):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf)
        self.salario = salario

    def mostrar_salario(self):
        print(f"Salário de {self.nome}: R$ {self.salario:.2f}")
