# Autor : Pietro Marchetti

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
