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
