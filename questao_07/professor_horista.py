# Autor : Pietro Marchetti

# Professor Horista herda de Professor e calcula o salário 
class ProfessorHorista(Professor):
    def __init__(self, nome, cpf, horas, valor_hora):
        salario = horas * valor_hora
        super().__init__(nome, cpf, salario)
