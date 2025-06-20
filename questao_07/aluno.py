# Autor : Pietro Marchetti

# Matrícula e notas
class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, notas):
        super().__init__(nome, cpf)  # chamada da classe Pessoa
        self.matricula = matricula
        self.notas = notas

    def mostrar_media(self):
        media = self.notas.calcular_media()
        print(f"Média de {self.nome}: {media:.2f}")
