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
