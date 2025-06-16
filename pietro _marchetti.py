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

import math  # importa uma biblioteca para fazer cálculo de raiz quadrada

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
