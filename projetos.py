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

print(f"Imposto devido: R$ {imposto_tot:.2f}")
print(f"Alíquota efetiva: {aliquota:.2f}%")

#--------------- Questão 04 -----------------

''' Conta quantas vezes os dados foram lançados ate sairem o mesmo número'''


import random

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
''' Fez um desenho de um céu a noite com estrelas de tamanhos e posições aleatórias '''

import turtle as t
import random 

def estrela(lado, cor='blue'):
    '''Desenha uma estrela de 5 pontas '''
    t.color(cor)
    i = 1
    while i <= 5:
        t.forward(lado)
        t.right(216)
        i += 1

def desenha_ceu(): #desenha um ceu estrelado com estrelas de tamanhos aleatorias em diversas posições
    t.speed('fastest') # velocidade máxima que é desenhado
    t.bgcolor('black') # cor do fundo do desenho 
    
    contador = 0
    while contador < 50:
        x = random.randint(-300, 300) # gera posições aleatorias para as estrelas 
        y = random.randint(-200, 200)# tambem gera posicoes aleatórias para as estrelas 
        
        t.penup() #levanta a caneta 
        t.goto(x, y)#movimenta a caneta para as posições
        t.pendown() # poe a caneta de volta para inciar novamente ao desenho 
        
        tamanho = random.randint(10, 40) # tamanho aleatório das estrelas 
        estrela(tamanho, 'blue')
        
        t.penup()  # levanta a caneta depois de desenhar
        
        contador += 1 #contador de estrelas desenhadas 

    t.done() #encerra o desenho 

# Chama a função para desenhar o céu
desenha_ceu()


#---------------- Questao 06 ---------------










#--------------- Questao 07 ----------------
''' Verifica se um numero inteiro é perfeito ou nao é perfeito '''

def num_perfeito(n):
   
    soma = 0 # armazena a soma dos divisores 
    i = 1 # divisor comeca em 1 
    while i <= n // 2 : # nenhum numero maior que a metade de n pode ser divisor de n
        if n % i == 0: # se o resto da divisao de n por i for zero , i é divisor de n 
            soma += i 
        i += 1
        # se n for um numero perfeito retorna True se nao retorna False 
    return soma == n

# Teste
num = int(input("Digite qualquer número inteiro positivo: "))
if num_perfeito(num):
    print("O número",num, "é perfeito!")
else:
    print("O número",num, "não perfeito!")


