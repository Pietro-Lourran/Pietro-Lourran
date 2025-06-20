# Autor : Pietro Marchetti

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
