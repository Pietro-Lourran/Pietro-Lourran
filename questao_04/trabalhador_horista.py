# trabalhadores que recebem por hora
class TrabalhadorHorista(Funcionario):
    def __init__(self, nome, cpf):
        super().__init__(nome, cpf)  # Chama o construtor da classe mãe
        self.__valor_hora = None
        self.__horas_mes = None

    # para o valor da hora trabalhada 
    def set_valor_hora(self, valor):
        if valor > 0:
            self.__valor_hora = valor
        else:
            print(f"Valor da hora inválido para {self.get_nome()}.")

    # número de horas trabalhadas no mês
    def set_horas_mes(self, horas):
        if horas >= 0:
            self.__horas_mes = horas
        else:
            print(f"Horas trabalhadas inválidas para {self.get_nome()}.")

    # calcula o salário 
    def calcular_pagamento(self):
        if self.__valor_hora is None or self.__horas_mes is None:
            print(f"Dados incompletos para {self.get_nome()}.")
        else:
            salario = self.__valor_hora * self.__horas_mes
            self.set_salario(salario)  # Salva o valor calculado
