
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
    
#---------------- Questao 04 --------------------
'''Verifica se dois retângulos se se colidem no plano 2D.'''

def colisao(retangulo_1, retangulo_2):
    # Cordenadas do primeiro retângulo
    x1_1 = retangulo_1[0]
    y1_1 = retangulo_1[1]
    x1_2 = retangulo_1[2]
    y1_2 = retangulo_1[3]
    
    # coordenadas do segundo retângulo
    x2_1 = retangulo_2[0]
    y2_1 = retangulo_2[1]
    x2_2 = retangulo_2[2]
    y2_2 = retangulo_2[3]
    
    # maximos e minimos de cada retângulo
    x1_min = min(x1_1, x1_2)
    x1_max = max(x1_1, x1_2)
    y1_min = min(y1_1, y1_2)
    y1_max = max(y1_1, y1_2)
    
    x2_min = min(x2_1, x2_2)
    x2_max = max(x2_1, x2_2)
    y2_min = min(y2_1, y2_2)
    y2_max = max(y2_1, y2_2)
    
    # Verifica se os retângulos estao separados ( direita e esquerda )
    if x1_max < x2_min or x2_max < x1_min:
        return False
    
    # verifica se ha um retangulo acima ou abaixo do outro
    if y1_max < y2_min or y2_max < y1_min:
        return False # nao colidem 
    
    
    return True #colidem 

# ----------------- Questao 05 ---------------


'''Função que devolve uma nova lista com os números 
que são maiores que n, em ordem crescente.'''

def maiores_que(lista, n):
    # Lista com os números maiores que n
    result = []

    # Para cada número dentro da lista
    for numero in lista:
        # número for maior que n
        if numero > n:
            # Coloca o numero n lista 
            result.append(numero)

    # orniza a lista com o resultado do menor pro maior
    result.sort()

    # retorna a lista 
    return result
# ------------- Questao 06 -------------------1-
'''Analisa a sequência de aminoácidos e retorna informações'''

def relatorio (seq):
    # Tamanho da lista 
    tamanho = len(seq)

    # Conta as LL
    ocorrencias_LL = seq.count('LL')

    # Posições GG e RR
    posicoes_GG = [i for i in range(len(seq)-1) if seq[i:i+2] == 'GG']
    posicoes_RR = [i for i in range(len(seq)-1) if seq[i:i+2] == 'RR']

    # contagem dos 100 primeiros aminoácidos
    primeiros_100 = seq[:100]

    # Substitui SSSR por AAAA
    seq_substituida = seq.replace('SSSR', 'AAAA')

    # Retornar tudo
    return {
        'tamanho': tamanho,
        'ocorrencias_LL': ocorrencias_LL,
        'posicoes_GG': posicoes_GG,
        'posicoes_RR': posicoes_RR,
        'primeiros_100': primeiros_100,
        'sequencia_substituida': seq_substituida
    }

# Sequência
sequencia_amino = "VRSSSRTPSDKPVAHVVANPQAEGQLQWINRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

# Usar a função
result = relatorio (sequencia_amino)

# Mostra o resultado
for k, v in result.items():
    print(f"{k}: {v}")

#--------------- Questao 07 ------------------

    '''Cria uma matriz com n linhas e m colunas, preenchida com zeros.'''
def cria_matriz(n, m):
    
    return [[0 for _ in range(m)] for _ in range(n)] #cria uma lista de n listas , cada lisa com m zeros 

    '''Soma duas matrizes A e B e retorna a matriz resultante.'''
    
def soma_matriz(A, B):
    
    if len(A) != len(B) or len(A[0]) != len(B[0]): # verifica se tem as mesmas direcoes 
        raise ValueError("As matrizes não possuem as mesmas dimensões.")
    
    n = len(A) #numero de linhas da matriz 
    m = len(A[0]) #numero de coluna 
    C = cria_matriz(n, m) #cria a matriz C com as mesmas dimensões comecando com zeros 
    
    for i in range(n): #percorre cada linha 
        for j in range(m): #percorre cada coluna 
            C[i][j] = A[i][j] + B[i][j] #soma os elementos de A e B
    return C #retorna a matriz resultante 

    '''Multiplica todos os elementos da matriz A por k e retorna  a matriz resultante'''
    
def multiplica_k (A, k):
    
    n = len(A) #numero de linhas 
    m = len(A[0]) #nuemro de colunas 
    C = cria_matriz(n, m)#cria a matriz
    
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] * k
    return C

    '''Multiplica duas matrizes A e B (se possível) e retorna a matriz resultante'''
    
def multiplica_matriz(A, B):
  
    linhas_A = len(A)
    colunas_A = len(A[0])
    linhas_B = len(B)
    colunas_B = len(B[0])
    
    if colunas_A != linhas_B:
        raise ValueError(f"Não é possível multiplicar: colunas de A ({colunas_A}) != linhas de B ({linhas_B})")
    
    C = cria_matriz(linhas_A, colunas_B)
    
    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(colunas_A):
                C[i][j] += A[i][k] * B[k][j]
    return C



