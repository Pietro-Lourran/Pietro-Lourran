
#----------------Questao 01--------------
def contas (valor, operacao):

    '''Função que realiza uma operação entre dois números(parâmetros),
    uma tupla com dois números e uma string.'''
    
    #Extraindo os dois números da tupla
    a = valor[0]
    b = valor[1]

    # Verifica cada operação pedida 
    if operacao == 'SOMA':  #soma
        return a + b
    elif operacao == 'MULT': #multiplicação 
        return a * b
    elif operacao == 'DIV': #divisão
        if b != 0:
            return a / b
        else:
            return 'Erro: Divisão por zero nao existe.'
    elif operacao == 'SUB': # subtração
        return a - b
    elif operacao == 'MOD': #módulo
        if b != 0:
            return a % b
        else:
            return 'Erro: Divisão por zero nao existe.'
    elif operacao == 'POT': # potencia 
        return a ** b
    else:
        # Operação não reconhecida
        return 'A operação informada não foi reconhecida.'
#-----------------Questao 02--------------
def analise_num (telefone):
    
    '''Função que processa um número de telefone brasileiro 
    e verifica se ele é válido.'''
    
    
    # Quantidade de dígitos
    tamanho = len(telefone)
    
    # Com DDD
    if tamanho == 10 or tamanho == 11:
        ddd = telefone[:2]
        numero = telefone[2:]
        
        # Verifica se o número sem DDD tem tamanho correto
        if len(numero) == 8 or len(numero) == 9:
            return (ddd, numero)
        else:
            return ('' , '')
    
    # Sem DDD
    elif tamanho == 8 or tamanho == 9:
        ddd = ''
        numero = telefone
        return (ddd, numero)
    
    # Tamanho inválido
    else:
        return ('' , '')
        
#-------------- Questao 03 ----------------

def avaliacao_alunos(dados):

    '''Função que avalia a situação de um aluno 
    com base em suas três notas.'''
 # tuplas com os dados necessários
    nome, nota1, nota2, nota3 = dados
    # média dos alunos 
    media = (nota1 + nota2 + nota3) / 3
    # média maior que 7 
    if media >= 7:
        situacao = 'aprovado, Parabéns!'
    elif media >= 5: #media maisor que 5 e menor que 7
        situacao = 'aprovado'
    else:
        situacao = 'reprovado' #media menor que 5
    
    # Retorna a media(com 1 casa decimal e situcao do aluno
    return (nome, f"{media:.1f}", situacao)
