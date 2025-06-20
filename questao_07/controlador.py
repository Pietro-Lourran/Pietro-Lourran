# Autor : Pietro Marchetti

# Controla listas de alunos e professores
class Controlador:
    def __init__(self):
        self.alunos = []
        self.professores = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def adicionar_professor(self, professor):
        self.professores.append(professor)

    def buscar_aluno_por_nome(self, nome):
        for aluno in self.alunos:
            if aluno.nome == nome:
                return aluno
        return None

    def buscar_professor_por_nome(self, nome):
        for professor in self.professores:
            if professor.nome == nome:
                return professor
        return None
