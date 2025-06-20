# Autor : Pietro Marchetti

# Teste
if __name__ == "__main__":
    # Alunos com notas
    a1 = Aluno("Vinicius", "12345678901", "A1", Notas(8, 7, 9))
    a2 = Aluno("Roberto", "23456789012", "A2", Notas(6, 5, 7))
    a3 = Aluno("Ana", "34567890123", "A3", Notas(9, 10, 10))

    # Professores
    p1 = Professor("Carlos Eduardo", "45678901234", 4000)
    p2 = Professor("Dalva", "56789012345", 5000)
    p3 = ProfessorHorista("Junior", "67890123456", 20, 100)  # 20 horas × R$100

    # Controlador
    sistema = Controlador()
    sistema.adicionar_aluno(a1)
    sistema.adicionar_aluno(a2)
    sistema.adicionar_aluno(a3)

    sistema.adicionar_professor(p1)
    sistema.adicionar_professor(p2)
    sistema.adicionar_professor(p3)

    # Mostra média dos alunos
    for nome in ["Vinicius", "Roberto", "Ana"]:
        aluno = sistema.buscar_aluno_por_nome(nome)
        if aluno:
            aluno.mostrar_media()

    # Mostra o salário dos professores
    for nome in ["Carlos Eduardo", "Dalva", "Junior"]:
        professor = sistema.buscar_professor_por_nome(nome)
        if professor:
            professor.mostrar_salario()
