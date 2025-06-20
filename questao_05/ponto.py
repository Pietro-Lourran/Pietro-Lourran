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
