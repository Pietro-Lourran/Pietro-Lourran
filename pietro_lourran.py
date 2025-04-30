#-------------- Questão 01 ---------------

''' Imprime o valor do salario total recebido após o reajuste de 9% 
e a bonificação de R$200.0 para salarios acima de R$3500.0'''

salario_inicial = float(input("Digite o salário do funcionário em R$: ")) # Solicita o salário incial sem abono e reajuste

valor_reajustado = salario_inicial * 0.09 + salario_inicial # Calculo do reajuste do salário inicial

if salario_inicial <= 3500.0: # Verifica se o salário original é menor ou igual a R$ 3500,00
   
    valor_reajustado += 200.0  # Adiciona o abono de R$ 200,00


print("Salário final recebido R$:",valor_reajustado) # Mostra o novo salário com reajuste ou/e abono

#--------------- Questão 02 ----------------

''' Retorna o valor da conta de agua de uma residencia 
a partir do consumo com uma assinatura basica de R$ 7.00'''

def calcular_agua(consumo):
    
    valor = 7.00 # Assinatura básica
    consumo_30 = (consumo - 10) * 1
    consumo_100 = (consumo - 30) * 2
    excedente = (consumo - 100) * 5
    
# Condicinando 
    if consumo <= 10:    # Se o consumo de agua for ate 10 m3
    
        return valor     # Retorna o valor da assinatura basica 

    elif consumo <= 30:    # Se o consumo for ate 30 m3 
        
        valor += consumo_30 # Valor de R$1,00 por cada m3 acima de 10

    elif consumo <= 100:   # Consumo ate 100 m3
        
        valor += 20 * 1 + consumo_100 # consumo ate 20 mais consumo ate 100

    # Consumo acima de 100 m3
    else:
    
        valor += 20 * 1 + 70 * 2 + excedente   # Consumo até 20 mais consumo ate 100 mais consumo acima de 100

    return valor

consumo = int(input("Digite o consumo de água em m³: "))
conta = calcular_agua(consumo)
print("O valor da conta de água é:R$", conta )

#--------------- Questão 03 ---------------

''' Retorna o valor do imposto de renda (IR)
 e a aliquota efetiva a partir da renda mensal tributavel'''


def calculo_de_ir (renda):
    
    # Define a base de calculo a partir das aliquotas e parcelas a deduzir
     
    if renda <= 2259.21: # p/ rendas menores que R$ 2259,21
        aliquota = 0
        deducao = 0
    elif renda <= 2826.65: # p/ rendas maiores que R$ 2259,21 e menores ou igual a R$ 2826,65
        aliquota = 0.075
        deducao = 169.44
    elif renda <= 3751.05: # p/ rendas maiores que R$ 2826,65 e menores ou igual a R$ 3571,07
        aliquota = 0.15
        deducao = 381.44
    elif renda <= 4664.68: # p/ rendas maiores que R$ 3751,05 e maiores ou igual a R$ 4664,68 
        aliquota = 0.225
        deducao = 662.77
    else: # p/ rendas maiores ou igual a R$ 4664,68
        aliquota = 0.275
        deducao = 896.00

    # Calculo do Imposto de Renda (IR)
    imposto_tot = renda * aliquota - deducao

    # Imposto de Renda nao pode ser negativo!
    # Garante que nao seja negativo
    if imposto_tot < 0: 
        imposto_tot = 0
        
    if renda > 0: #Se a renda for maior que zero, calcula a aliquota efetiva
    
        ali_efetiva = (imposto_tot / renda) * 100 # Calculo em %
        
    else: # se a renda for igual a zero a aliquota tambem sera zero
        ali_efetiva = 0

    return imposto_tot, ali_efetiva

renda = float(input("Digite a renda mensal em R$: "))
# Função p/ calcular
imposto_tot, aliquota = calculo_de_ir (renda)

print(f"Imposto: R$ {imposto_tot:.2f}")# comando .2f garante que o resultado tera duas casas decimais 
print(f"Alíquota efetiva: {aliquota:.2f}%")

#--------------- Questão 04 -----------------

''' Conta quantas vezes os dados foram lançados ate sairem o mesmo número'''


import random #importa random da biblioteca 

def dados():
    cont = 0  # Começa a contagem de vezes que o dado foi jogado


    while True:  # Cria um laço que que vai rodar infinitamente
        dado_a = random.randint(1, 6) # Sorteia um número de 1 a 6 para o primeiro dado
        dado_b = random.randint(1, 6) # Sorteia um número de 1 a 6 para o segundo dado
        cont += 1 # Conta uma jogada que foi feita
        
        # Encerra o laço criado quando os numeros dos dados forem iguais
        # Termina o jogo
        if dado_a == dado_b:
            break  

    print(cont, "jogadas para os dois dados mostraram o número:" , dado_a)

dados() 

#----------------- Questão 05 ----------------
''' Faz um desenho de um céu a noite com estrelas de tamanhos e posições aleatórias '''

import turtle as d # importa o comando turtle da biblioteca 
import random  # importa o comando random da biblioteca 

def estrela(lado, cor='blue'):
   
    #Desenha uma estrela de 5 pontas 
    d.color(cor)
    i = 1
    while i <= 5:
        d.forward(lado)
        d.right(216)
        i += 1

def desenha_ceu(): #desenha um ceu estrelado com estrelas de tamanhos aleatorias em diversas posições
    d.speed('fastest') # velocidade máxima que é desenhado
    d.bgcolor('black') # cor do fundo do desenho 
    
    contador = 0
    while contador < 50:
        x = random.randint(-300, 300) # gera posições aleatorias para as estrelas 
        y = random.randint(-200, 200)# tambem gera posicoes aleatórias para as estrelas 
        
        d.penup() #levanta a caneta 
        d.goto(x, y)#movimenta a caneta para as posições
        d.pendown() # poe a caneta de volta para inciar novamente ao desenho 
        
        tamanho = random.randint(10, 40) # tamanho aleatório das estrelas 
        estrela(tamanho, 'blue')
        
        d.penup()  # levanta a caneta depois de desenhar
        
        contador += 1 #contador de estrelas desenhadas 

    d.done() #encerra o desenho 

# Chama a função para desenhar o céu
desenha_ceu()


#---------------- Questao 06 ---------------
''' Desenha uma imagem tipo um tabuleiro de xadrez com as cores, vermelho e preto'''

import turtle as d

def pintar_casa(tam, cor):
    #Desenha uma casa quadrada do tabuleiro com o tamanho e cor definidos
    d.begin_fill() # inicia o preenchimento das casas do tabuleiro
    d.fillcolor(cor) #define a cor 
    lado = 0
    while lado < 4: # desenha um quadrado 
        d.forward(tam)
        d.left(90)
        lado += 1
    d.end_fill() # finaliza o preenchimento 

def desenhar_tabuleiro(casa_1='red', casa_2 ='black'):
    #Cria um tabuleiro estilo xadrez com cores alternadas usando turtle
    d.speed('fastest') # velocidade do desenho
    d.bgcolor('black') # cor de fundo 
    d.hideturtle() # oculta o ponteiro 
    
# Determina que o tabuleiro é 8x8 e o tamanho de cada casa do tabuleiro
    tamanho_casa = 40
    total_linhas = 8
    total_colunas = 8
#coordenadas iniciais do desenho
    origem_x = -160
    origem_y = 160

    linha_atual = 0
    while linha_atual < total_linhas:
        coluna_atual = 0
        d.penup()
        d.goto(origem_x, origem_y - linha_atual * tamanho_casa) # move o cursor para o inicio 
        while coluna_atual < total_colunas:
            x = origem_x + coluna_atual * tamanho_casa # calcula a posicao x da casa 
            y = origem_y - linha_atual * tamanho_casa # calcula a poiscao y da casa 
            d.goto(x, y) #move o cursor para as posições

            # alterna as cores das casas do tabuleiro xadrez
            if (linha_atual + coluna_atual) % 2 == 0:
                cor_casa = casa_1
            else:
                cor_casa = casa_2

            d.pendown()
            pintar_casa(tamanho_casa, cor_casa) # desenha cada casa com suas respectivas cores
            d.penup()
            coluna_atual += 1
        linha_atual += 1

    d.done()










#--------------- Questao 07 ----------------
''' Verifica se um numero inteiro é perfeito ou nao é perfeito '''

def num_perfeito(n):
   
    somatorio = 0 # armazena a soma dos divisores 
    i = 1 # divisor comeca em 1 
    while i <= n // 2 : # nenhum numero maior que a metade de n pode ser divisor de n
        if n % i == 0: # se o resto da divisao de n por i for zero , i é divisor de n 
            somatorio += i 
        i += 1
        # se n for um numero perfeito retorna True se nao retorna False 
    return somatorio == n

# Teste
num = int(input("Digite qualquer número inteiro positivo: "))
if num_perfeito(num):
    print("O número",num, "é perfeito!")
else:
    print("O número",num, "não perfeito!")
   
#---------------- Questão 08 --------------
''' Soma todos os numeros primos menores que n'''

def total_primos(n):
    def test_primo(num):  # verifica se o número é primo
        if num < 2:  # todo número menor que 2 não é primo
            return False
        divisor = 2
        while divisor * divisor <= num:  # testa divisibilidade até a raiz quadrada
            if num % divisor == 0:
                return False
            divisor += 1
        return True

    somatorio = 0
    i = 2  # começa com o primeiro número primo
    while i < n:
        if test_primo(i):
            somatorio += i
        i += 1

    print("A soma dos números primos menores que", n, "é", somatorio)

# Exemplo de chamada da função:
total_primos(20)  # Você passa o número direto aqui

#--------------- Questao 09 ---------------
'''  Calcula a taxa de juros compostos ao longo dos anos.'''

    #Parâmetros:
          #p_inicial --> Valor aplicado
          #r_juros --> % de juros ao ano
          #anos --> Duração da aplicação em anos.


def calc_juros_comp(p_valor_inicial, r_juros, anos):

    
    # Exibe o saldo atualizado ano após ano.
    

    # Da inicio ao saldo com o valor inicial investido
    saldo = p_valor_inicial

    # Organiza o ano e o valor acumulado 
    print("Ano  |  Valor acumulado")
    
    # Inicia o contador de anos ; cont --> contador
    cont = 1

    # loop que faz a contagem dos anos 
    while cont <= anos:
      
        # Saldo aplicado com os juros 
        saldo *= (1 + r_juros)

        # ano atual e o saldo formatado com duas casas decimais
        print(f"{cont:<5}  R$ {saldo:.2f}")

        # adiciona o o contador para passar os anos
        cont += 1

# Exemplo 
calc_juros_comp(1000.00, 0.05, 10)

#---------------- Questao 10 --------------
def calcula_invest():
    # solicita os valor inicial investido , o aporte mensal e o objetivo
    ap_inicial = float(input("Valor que deseja investir inicialmente: "))  # aporte inicial 
    ap_mensal = float(input("Aporte mensal: "))  # valor que será investido todo mês
    valor_esperado = float(input("Valor esperado ao fim do investimento: "))

    # entrada para o tempo investimento ano/mes
    anos = int(input("Quantos anos de investimento: "))
    meses = int(input("Quantos meses adicionais: "))

    # Calcula o tempo de meses
    total_meses = anos * 12 + meses

    # solicita a taxa de juros mensal ou anual
    taxa = float(input("Taxa de juros em %): ")) / 100  # converte em %
    tipo = input("A taxa de juros é anual ou mensal? ")

    if tipo == "anual":  # converte a taxa anual em mensal
        taxa = (1 + taxa) ** (1 / 12) - 1

    # poupança definida como 0,5%
    taxa_poup = 0.005

    # Saldos iniciais
    saldo_investimento = ap_inicial
    saldo_poupanca = ap_inicial

    mes = 1
    while mes <= total_meses:
        saldo_investimento = saldo_investimento * (1 + taxa) + ap_mensal  # aplica o juros e o aporte mensal no saldo do investimento 
        saldo_poupanca = saldo_poupanca * (1 + taxa_poup) + ap_mensal  # aplica o juros da poupança e do aporte mensal 
        print(f"Mês {mes} - Saldo: R$ {saldo_investimento:.2f} | Poupança: R$ {saldo_poupanca:.2f}")
        mes += 1  # avança os meses 

    # Calcula o tempo para alcançar o objetivo 
    saldo_temp = ap_inicial  # reinicia o valor inicial 
    meses_ate_valor_esperado = 0  # zera o contador
    
    while saldo_temp < valor_esperado:
        saldo_temp = saldo_temp * (1 + taxa) + ap_mensal
        meses_ate_valor_esperado += 1

    # converte o tempo necessário de meses para anos 
    anos_finais = meses_ate_valor_esperado // 12
    meses_finais = meses_ate_valor_esperado % 12

    # mostra o relatório final 
    print(f"\nPara atingir o objetivo de R$ {valor_esperado:.2f}") # comando\n quebra a linha 
    print(f"Você precisará de {anos_finais} anos e {meses_finais} meses.")
    print(f"Saldo final com investimento: R$ {saldo_investimento:.2f}") #comando .2f ganrante que tenha 2 casas decimais no resultado
    print(f"Saldo final com a poupança: R$ {saldo_poupanca:.2f}")

# Executa a função
calcula_invest()
