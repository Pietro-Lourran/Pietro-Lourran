# Autor : Pietro Marchetti

''' Cria uma classe Funcionario com os atributos privados nome, 
cpf e salario; e um construtor que deve receber como parâmetro nome e cpf. Todos os atributos devem ter propriedades (getters) definidos.'''

# Classe que representa um funcionário aleatorio
class Funcionario:
    def __init__(self, nome, cpf):
        
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = 0.0  # Salário inicia em zero reais

    # Nome
    def get_nome(self):
        return self.__nome

    # CPF
    def get_cpf(self):
        return self.__cpf

    # Salário
    def get_salario(self):
        return self.__salario

    # para o salário (método usado pelas classes filhas)
    def set_salario(self, valor):
        self.__salario = valor
