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

# Programa principal
renda = float(input("Digite a renda mensal em R$: "))

imposto_tot, aliquota = calculo_de_ir (renda)

print(f"Imposto devido: R$ {imposto_tot:.2f}")
print(f"Alíquota efetiva: {aliquota:.2f}%")

