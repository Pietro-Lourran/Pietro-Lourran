#---------------- Questão 01 ----------------
''' Cria uma classe que calcula a quantodade necessaria, 
gastos, km percorridos, etc'''

# Define a Classe 

class Veiculo:
    # executa quando um novo carro é criado
    def __init__(self, economia, limiteTanque):
        self.km_por_litro = economia          # km rodadod por litro de gasolina (consumo)
        self.tanque_max = limiteTanque        # Capacidade máxima do tanque de combustível
        self.tanque_atual = 0                 # Inicialmente o tanque começa vazio

    # simula o carro indo a uma certa distância
    def dirigir(self, destino_km):
        # Tanque vazio 
        if self.tanque_atual <= 0:
            print("Sem combustível. Abasteça!")
            return
        
        # Calculo de quanta gasolina será necessário para ir ate certa distância
        gasto = destino_km / self.km_por_litro
        
        # Verifica se o combustível suficiente ou nao
        if gasto > self.tanque_atual:
            # Se não for suficiente, mostra até onde pode ir com o que tem no tanque 
            print(f"Só dá para ir até {self.tanque_atual * self.km_por_litro:.1f} km.")
        else:
            # Se for suficiente
            self.tanque_atual -= gasto
            print(f"Distância de {destino_km} km concluída! Gasolina restante no tanque: {self.tanque_atual:.2f} L")

    # Ver quanto de combustível ainda tem no tanque
    def getCombustivel(self):
        print(f"Combustível atual: {self.tanque_atual:.2f} litros")
        return self.tanque_atual

    # abastecer o carro com uma certa quantidade de litros
    def encher(self, quantidade):
        # Não abastece caso tenha mais de zero 
        if quantidade <= 0:
            print("Quantidade inválida!")
            return
        
        # verifica se  ultrapassa a capacidade do tanque
        if self.tanque_atual + quantidade > self.tanque_max:
            # se ultrapassa abastece até o máximo permitido
            sobrando = self.tanque_max - self.tanque_atual
            self.tanque_atual = self.tanque_max
            print(f"Tanque cheio. Só couberam {sobrando:.2f} L")
        else:
            # se nao, abastece normalmente
            self.tanque_atual += quantidade
            print(f"Abastecido com {quantidade:.2f} L. Agora tem {self.tanque_atual:.2f} L")

# Função principal
def main():
    print("Criando o Veículo")
    meu_carro = Veiculo(economia=12, limiteTanque=45)  

    meu_carro.getCombustivel()      
    meu_carro.dirigir(50)             

    meu_carro.encher(20)              
    meu_carro.dirigir(100)            

    meu_carro.getCombustivel()       
    meu_carro.encher(30)              

    meu_carro.dirigir(500)            
    meu_carro.getCombustivel()       

# Verifica se  está sendo executado diretamente 
if __name__ == "__main__":
    main()

#---------------- Questao 02 ----------------
''' Cria uma Classe para verificar os tipos de triangulos, 
area , perimetro dos triangulos'''

import math 

# Classe Triangulo
class Triangulo:
    # cria um triângulo com os lados a, b e c
    def __init__(self, a, b, c):
        # Verifica se os lados formam um triângulo válido
        if self.ehValido(a, b, c):
            self.a = a
            self.b = b
            self.c = c
        else:
            print(" Os lados informados não formam um triângulo válido!")
            self.a = self.b = self.c = 0  # Coloca tudo como zero se não for válido

    # Verifica se o triângulo é válido
    def ehValido(self, a, b, c):
        # Um triângulo é válido se a soma de dois lados for maior que o terceiro
        if a + b > c and a + c > b and b + c > a:
            return True
        else:
            return False

    # Tipo do triângulo
    def tipoTriangulo(self):
        if self.a == self.b == self.c:
            return "Equilátero (3 lados iguais)"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Isósceles (2 lados iguais)"
        else:
            return "Escaleno (3 lados diferentes)"

    # Calculs o perímetro m
    def calculaPerimetro(self):
        return self.a + self.b + self.c

    # Calcula a área usando a fórmula de Heron 
    def calculaArea(self):
        p = self.calculaPerimetro() / 2  # semiperímetro 
        area = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return area

# Testa a classe Triangulo
def main():
    #Triangulo equilatero
    print("Triângulo #1:")
    t1 = Triangulo(5, 5, 5)  
    print("Tipo:", t1.tipoTriangulo())
    print("Perímetro:", t1.calculaPerimetro())
    print("Área:", round(t1.calculaArea(), 2))
    print()
#Triangulo  isósceles
    print("Triângulo #2:")
    t2 = Triangulo(6, 6, 4)  
    print("Tipo:", t2.tipoTriangulo())
    print("Perímetro:", t2.calculaPerimetro())
    print("Área:", round(t2.calculaArea(), 2))
    print()
#Traingulo equilatero
    print("Triângulo #3:")
    t3 = Triangulo(7, 5, 6)  
    print("Tipo:", t3.tipoTriangulo())
    print("Perímetro:", t3.calculaPerimetro())
    print("Área:", round(t3.calculaArea(), 2))
    print()
#Triangulo Invalido
    print("Triângulo #4 (inválido):")
    t4 = Triangulo(2, 2, 10)  
    print("Tipo:", t4.tipoTriangulo())
    print("Perímetro:", t4.calculaPerimetro())
    print("Área:", round(t4.calculaArea(), 2))

if __name__ == "__main__":
    main()

#-------------- Questao 03 --------------

import math
# Define a classe que representa um ponto 
class Ponto2D:
    def __init__(self, x=0, y=0): #se nenhum valor for informado , o pontk esta na origem 
        self.x = x
        self.y = y
# calcula a distância 
    def distancia(self, outro):
        dx = outro.x - self.x
        dy = outro.y - self.y
        return math.sqrt(dx**2 + dy**2)
# retorna a representação do ponto 
    def __str__(self):
        return f"({self.x}, {self.y})"
# testa a classe 
def main():
    print("== Distância entre os Pontos 2D ==")

    p1 = Ponto2D()  # Origem
    p2 = Ponto2D(3, 4)
    p3 = Ponto2D(-1, -1)

    print("Ponto A:", p1)
    print("Ponto B:", p2)
    print("Ponto C:", p3)

    print(f"Distância de A até B: {p1.distancia(p2):.2f}")
    print(f"Distância de B até C: {p2.distancia(p3):.2f}")
# finaliza o programa 
if __name__ == "__main__":
    main()
#----------------- Questao 4 ----------------
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


# salário fixo
class TrabalhadorAssalariado(Funcionario):
    # definine o salário mensal
    def definir_salario(self, salario):
        if salario > 0:
            self.set_salario(salario)  # Usa o método da classe mãe
        else:
            print(f"Salário inválido para {self.get_nome()}.")


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

# Lista que guarda os funcionários
funcionarios = []

# três trabalhadores assalariados
a1 = TrabalhadorAssalariado("Pedro", "12345678900")
a1.definir_salario(3000)
funcionarios.append(a1)

a2 = TrabalhadorAssalariado("Julia", "23456789011")
a2.definir_salario(4200)
funcionarios.append(a2)

a3 = TrabalhadorAssalariado("Rafael", "34567890122")
a3.definir_salario(3800)
funcionarios.append(a3)

# três trabalhadores horistas
h1 = TrabalhadorHorista("Lucas", "45678901233")
h1.set_valor_hora(50)
h1.set_horas_mes(160)
h1.calcular_pagamento()
funcionarios.append(h1)

h2 = TrabalhadorHorista("Beatriz", "56789012344")
h2.set_valor_hora(40)
h2.set_horas_mes(150)
h2.calcular_pagamento()
funcionarios.append(h2)

h3 = TrabalhadorHorista("Amanda", "67890123455")
h3.set_valor_hora(60)
h3.set_horas_mes(140)
h3.calcular_pagamento()
funcionarios.append(h3)

# Imprime os pagamentos de todos os funcionários
print("\nPagamentos do mês:\n")
for f in funcionarios:
    print(f"{f.get_nome()}: R$ {f.get_salario():.2f}")

#--------------- Questao 5 -----------------
''' imprime pontos escolhidos, a soma dos pontos, a subtração 
multiplicação e a multiplicação por um escalar '''

# Classe representando um ponto
class Ponto:
    def __init__(self, x=0, y=0):
        
        self.x = x #coordenada x do ponto
        self.y = y # coordenada y do ponto

    # Imprime o ponto
    def __str__(self):
        return f"({self.x}, {self.y})"

    # soma de dois pontos 
    def __add__(self, outro):
        return Ponto(self.x + outro.x, self.y + outro.y)

    # Subtração de dois pontos 
    def __sub__(self, outro):
        return Ponto(self.x - outro.x, self.y - outro.y)

    # Produto escalar entre dois pontos
    def __mul__(self, outro):
        if isinstance(outro, Ponto):
            return self.x * outro.x + self.y * outro.y
        else:
            return NotImplemented

    # Multiplicação de escalar por um ponto
    def __rmul__(self, escalar):
        return Ponto(escalar * self.x, escalar * self.y)

    # Como usar 

if __name__ == "__main__":
    # Escolha os pontos 
    p1 = Ponto(1, 3)
    p2 = Ponto(2, 1)

    # Imprime os pontos
    print("P1 =", p1)          
    print("P2 =", p2)           

    # Soma dos pontos 
    soma = p1 + p2
    print("P1 + P2 =", soma)   

    # Subtração dos pontos 
    sub = p1 - p2
    print("P1 - P2 =", sub)     

    # Produto escalar 
    produto = p1 * p2
    print("P1 * P2 =", produto) 

    # Escalar * ponto 
    escalar = 3
    multiplicado = escalar * p1
    print(f"{escalar} * P1 =", multiplicado)  

#------------------- Questao 6 --------------
''' Imprime um horario em HH:MM:SS e mensagens de aviso caso valores sejam inválidos 
para a hora , minutos e segundo'''
class Relogio:
    def __init__(self, h, m, s):
        # Verifica se as horas são válidas
        if 0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60:
            self.h = h
            self.m = m
            self.s = s
        else:
            print("Horario digitado invalido !")
            self.h = self.m = self.s = None

    def __str__(self):
        # Retorna o horário
        if self.h is None:
            return "Horário inválido"
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def total_segundos(self):
        # Converte para segundos
        return self.h * 3600 + self.m * 60 + self.s

    def __add__(self, outro):
        # Soma duas horas e retorna 
        total = self.total_segundos() + outro.total_segundos()
        h = (total // 3600) % 24
        m = (total % 3600) // 60
        s = total % 60
        return Relogio(h, m, s)

    def __sub__(self, outro):
        # Subtrai dois horários se o primeiro for maior ou igual
        if self.total_segundos() < outro.total_segundos():
            print("O primeiro horario dever ser maior ou igual ao segundo")
            return None
        total = self.total_segundos() - outro.total_segundos()
        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60
        return Relogio(h, m, s)

    def __eq__(self, outro):
        # confere se dois horários são iguais ou nao 
        return self.total_segundos() == outro.total_segundos()

    def __lt__(self, outro):
        # confere se este horário é menor que o outro
        return self.total_segundos() < outro.total_segundos()

    def __gt__(self, outro):
        # confere se este horário é maior que o outro
        return self.total_segundos() > outro.total_segundos()
# como usar (exemplo)

r0 = Relogio(12, 65, 54)  # Inválido
r1 = Relogio(17, 30, 28)
r2 = Relogio(20, 0, 30)

print(r1)          
print(r2)          

r3 = r1 + r2
print(r3)          

r4 = r3 - r2       
print(r4)          

r5 = r2 - r3       
print(r5)          

print(r1 == r2)    
r6 = Relogio(18, 37, 32)
print(r1 == r6)    

print(r1 > r3)    
print(r2 < r3)     
print(r2 > r3)     
print(r2 < r3)     


#---------------- Questao 07 ---------------
''' Armazena dados de alunos e professores e calcula as medias dos alunos'
# Classe básica que representa uma pessoa
class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

# Guarda 3 notas e calcula a média
class Notas:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def calcular_media(self):
        return (self.n1 + self.n2 + self.n3) / 3

# Matrícula e notas
class Aluno(Pessoa):
    def __init__(self, nome, cpf, matricula, notas):
        super().__init__(nome, cpf)  # chamada da classe Pessoa
        self.matricula = matricula
        self.notas = notas

    def mostrar_media(self):
        media = self.notas.calcular_media()
        print(f"Média de {self.nome}: {media:.2f}")

# Classe Professor e Pessoa e salário
class Professor(Pessoa):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf)
        self.salario = salario

    def mostrar_salario(self):
        print(f"Salário de {self.nome}: R$ {self.salario:.2f}")

# Professor Horista herda de Professor e calcula o salário 
class ProfessorHorista(Professor):
    def __init__(self, nome, cpf, horas, valor_hora):
        salario = horas * valor_hora
        super().__init__(nome, cpf, salario)

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






