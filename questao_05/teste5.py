# Autor : Pietro Marchetti

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
