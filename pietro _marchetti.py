# Definição da classe CarroDoPietro
class CarroDoPietro:
    # Construtor: é executado automaticamente quando criamos um novo carro
    def __init__(self, economia, limiteTanque):
        self.km_por_litro = economia          # Quantos km o carro percorre por litro (consumo)
        self.tanque_max = limiteTanque        # Capacidade máxima do tanque de combustível
        self.tanque_atual = 0                 # Inicialmente o tanque começa vazio

    # Método para simular o carro dirigindo uma certa distância (em km)
    def dirigir(self, destino_km):
        # Se o tanque estiver vazio, não é possível dirigir
        if self.tanque_atual <= 0:
            print("Sem combustível. Abasteça antes de viajar!")
            return
        
        # Calcula quanto combustível será necessário para percorrer a distância
        gasto = destino_km / self.km_por_litro
        
        # Verifica se há combustível suficiente
        if gasto > self.tanque_atual:
            # Se não tiver, mostra até onde é possível ir com o que tem
            print(f"Ops! Só dá pra andar até {self.tanque_atual * self.km_por_litro:.1f} km com o que tem.")
        else:
            # Se tiver combustível suficiente, subtrai o gasto do tanque atual
            self.tanque_atual -= gasto
            print(f"Viagem de {destino_km} km feita! Gasolina agora: {self.tanque_atual:.2f} L")

    # Método para ver quanto de combustível ainda tem no tanque
    def ver_combustivel(self):
        print(f"Combustível atual: {self.tanque_atual:.2f} litros")
        return self.tanque_atual

    # Método para abastecer o carro com uma quantidade de litros
    def encher(self, quantidade):
        # Não permite abastecer com valores negativos ou zero
        if quantidade <= 0:
            print("Quantidade inválida!")
            return
        
        # Verifica se o abastecimento ultrapassa a capacidade do tanque
        if self.tanque_atual + quantidade > self.tanque_max:
            # Se ultrapassar, só abastece até o máximo permitido
            sobrando = self.tanque_max - self.tanque_atual
            self.tanque_atual = self.tanque_max
            print(f"Tanque cheio. Só couberam {sobrando:.2f} L")
        else:
            # Caso contrário, abastece normalmente
            self.tanque_atual += quantidade
            print(f"Abastecido com {quantidade:.2f} L. Agora tem {self.tanque_atual:.2f} L")

# Função principal para testar os métodos da classe
def main():
    print("🚗 Criando o carro do Pietro...")
    meu_carro = CarroDoPietro(economia=12, limiteTanque=45)  # Consumo: 12 km/L | Tanque: 45 L

    meu_carro.ver_combustivel()       # Mostra o combustível (deve estar 0)
    meu_carro.dirigir(50)             # Tenta dirigir 50 km (sem combustível)

    meu_carro.encher(20)              # Abastece com 20 L
    meu_carro.dirigir(100)            # Dirige 100 km (gasta aprox. 8.33 L)

    meu_carro.ver_combustivel()       # Mostra o combustível restante
    meu_carro.encher(30)              # Tenta abastecer 30 L (deve encher só até o limite)

    meu_carro.dirigir(500)            # Tenta dirigir 500 km (deve avisar se não conseguir)
    meu_carro.ver_combustivel()       # Mostra o combustível final

# Verifica se o script está sendo executado diretamente (não importado)
if __name__ == "__main__":
    main()
