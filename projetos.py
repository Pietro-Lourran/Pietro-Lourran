#-------------- Questão 01 ---------------

''' Imprime o valor do salario total recebido após o reajuste de 9% 
e a bonificação de R$200.0 para salarios acima de R$3500.0'''

salario_inicial = float(input("Digite o salário do funcionário em R$: ")) # Solicita o salário incial sem abono e reajuste

valor_reajustado = salario_inicial * 0.09 + salario_inicial # Calculo do reajuste do salário inicial

if salario_inicial <= 3500.0: # Verifica se o salário original é menor ou igual a R$ 3500,00
   
    valor_reajustado += 200.0  # Adiciona o abono de R$ 200,00


print("Salário final recebido R$:",valor_reajustado) # Mostra o novo salário com reajuste ou/e abono