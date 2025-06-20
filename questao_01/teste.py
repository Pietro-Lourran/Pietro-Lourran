
# Autor : Pietro Marchetti


 # teste 
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
