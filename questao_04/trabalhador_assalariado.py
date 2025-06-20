# salário fixo
class TrabalhadorAssalariado(Funcionario):
    # definine o salário mensal
    def definir_salario(self, salario):
        if salario > 0:
            self.set_salario(salario)  # Usa o método da classe mãe
        else:
            print(f"Salário inválido para {self.get_nome()}.")
