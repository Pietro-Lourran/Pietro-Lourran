#----------------Questao 01--------------
def contas (valor, operacao):

    '''Função que realiza uma operação entre dois números(parâmetros),
    uma tupla com dois números e uma string.'''
    
    #Extrai os dois números da tupla
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
    # Analisa os números maiores que n
    maiores = []
    for a in lista:
        if a > n:
            maiores += [a]  # adiciona um elemento na lista

    # Retorna a lista 
    return sorted(maiores)

# ------------- Questao 06 -------------------1-
'''Analisa uma sequência de aminoácidos e retorna informações sobre'''
 def relatorio(seq):
    tamanho = len(seq)
    ocorrencias_LL = seq.count('LL')
    posicoes_GG = [i for i in range(len(seq)-1) if seq[i:i+2] == 'GG']
    posicoes_RR = [i for i in range(len(seq)-1) if seq[i:i+2] == 'RR']
    primeiros_100 = seq[:100]
    seq_substituida = seq.replace('SSSR', 'AAAA')

    return {
        'tamanho': tamanho,
        'ocorrencias_LL': ocorrencias_LL,
        'posicoes_GG': posicoes_GG,
        'posicoes_RR': posicoes_RR,
        'primeiros_100': primeiros_100,
        'sequencia_substituida': seq_substituida
    }
    #entrada 
sequencia_amino = input("Digite a sequência de aminoácidos ou letras: ").strip().upper()

resultado = relatorio(sequencia_amino)

for k, v in resultado.items():
    print(f"{k}: {v}")


#--------------- Questao 07 ------------------

    '''Cria uma matriz com n linhas e m colunas, preenchida com zeros.'''
def cria_matriz(n_linhas, n_colunas):
    
    return [[0 for _ in range(n_colunas)] for _ in range(n_linhas)] #cria uma lista de n listas , cada lista com m zeros 

    #Soma duas matrizes A e B e retorna a matriz resultante.
    
def soma_matriz(A, B):
    
    if len(A) != len(B) or len(A[0]) != len(B[0]): # verifica se tem as mesmas direcoes 
        raise ValueError("As matrizes não possuem as mesmas dimensões.")
    
    n_linhas = len(A) #numero de linhas da matriz 
    n_colunas = len(A[0]) #numero de coluna 
    C = cria_matriz(n_linhas, n_colunas) #cria a matriz C com as mesmas dimensões comecando com zeros 
    
    for i in range(n_linhas): #percorre cada linha 
        for j in range(n_colunas): #percorre cada coluna 
            C[i][j] = A[i][j] + B[i][j] #soma os elementos de A e B
    return C #retorna a matriz resultante 

    '''Multiplica todos os elementos da matriz A por k e retorna  a matriz resultante'''
    
def multiplica_k (A, k):
    
    n_linhas = len(A) #numero de linhas 
    n_colunas = len(A[0]) #nuemro de colunas 
    C = cria_matriz(n_linhas, n_colunas)#cria a matriz
    
    for i in range(n_linhas):
        for j in range(n_colunas):
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




#------------------- Questao 08 -------------------
def relatorio(dados):
    
    medias = {}  # média de cada categoria 

    for categoria in dados:  # Para cada categoria (ex: "Habitação") dentro dos dados
        print(f"\nCategoria: {categoria}")  # Mostra o nome da categoria
        estados = dados[categoria]  # Pega o dicionário de estados e valores dessa categoria

        # lista com os (estado, ipca), sem o Brasil
        sem_brasil = []  
        for estado in estados:  
            if estado != 'Brasil':  
                sem_brasil.append((estado, estados[estado]))  # Exemplo: ('Rio Branco', 0.55)

        # menor e o maior são o primeiro da lista
        menor_estado, menor_ipca = sem_brasil[0]
        maior_estado, maior_ipca = sem_brasil[0]

        soma_ipca = 0  # soma de todos os IPCAs 

        # percorre a lista percorremos a lista
        for estado, ipca in sem_brasil:
            if ipca < menor_ipca:  # IPCA menor 
                menor_ipca = ipca
                menor_estado = estado
            if ipca > maior_ipca:  # IPCA maior
                maior_ipca = ipca
                maior_estado = estado

            soma_ipca += ipca  # somam com o IPCA atual

        media_ipca = soma_ipca / len(sem_brasil)  # calcula a média
        medias[categoria] = media_ipca 

        # imorime os resultados
        print(f"  a) Estado com menor IPCA: {menor_estado} ({menor_ipca:.2f}%)")
        print(f"  b) Estado com maior IPCA: {maior_estado} ({maior_ipca:.2f}%)")
        print(f"  c) Média do IPCA: {media_ipca:.2f}%")

    # categoria com a maior e a menor média
    categorias_tuplas = list(medias.items()) 

    maior_categoria, maior_media = categorias_tuplas[0]
    menor_categoria, menor_media = categorias_tuplas[0]

    # compara as categorias 
    for categoria, media in categorias_tuplas:
        if media > maior_media:
            maior_media = media
            maior_categoria = categoria
        if media < menor_media:
            menor_media = media
            menor_categoria = categoria

    # resumo final
    print("\nResumo final:")
    print(f"  d) Categoria com maior IPCA médio: {maior_categoria} ({maior_media:.2f}%)")
    print(f"  e) Categoria com menor IPCA médio: {menor_categoria} ({menor_media:.2f}%)")

# dados para analise 
dados_ipca = {
    'Índice geral': {
        'Rio Branco': 0.55,
        'São Luís': 0.45,
        'Aracaju': 0.39,
        'Campo Grande': 0.60,
        'Goiânia': 0.14,
        'Brasília': 0.40,
        'Belém': 0.44,
        'Fortaleza': 0.60,
        'Recife': 0.22
    },
    'Alimentação e bebidas': {
        'Rio Branco': 0.01,
        'São Luís': 0.56,
        'Aracaju': 1.38,
        'Campo Grande': 0.83,
        'Goiânia': 1.54,
        'Brasília': 0.59,
        'Belém': 0.59,
        'Fortaleza': 0.55,
        'Recife': 0.64
    },
    'Habitação': {
        'Rio Branco': 0.21,
        'São Luís': 0.61,
        'Aracaju': 0.14,
        'Campo Grande': 0.66,
        'Goiânia': 0.15,
        'Brasília': -0.17,
        'Belém': -0.18,
        'Fortaleza': 0.93,
        'Recife': -0.30
    },
    'Artigos de residência': {
        'Rio Branco': 0.31,
        'São Luís': 0.41,
        'Aracaju': 1.68,
        'Campo Grande': 0.42,
        'Goiânia': 0.12,
        'Brasília': -0.35,
        'Belém': 0.04,
        'Fortaleza': 0.60,
        'Recife': -0.06
    },
    'Vestuário': {
        'Rio Branco': 0.51,
        'São Luís': 0.24,
        'Aracaju': 1.15,
        'Campo Grande': 1.33,
        'Goiânia': 0.27,
        'Brasília': 0.33,
        'Belém': 0.77,
        'Fortaleza': 0.50,
        'Recife': 0.57
    },
    'Transportes': {
        'Rio Branco': -0.38,
        'São Luís': 1.01,
        'Aracaju': 1.20,
        'Campo Grande': 0.95,
        'Goiânia': 1.03,
        'Brasília': -0.85,
        'Belém': -1.45,
        'Fortaleza': -0.20,
        'Recife': -0.66
    },
    'Saúde e cuidados pessoais': {
        'Rio Branco': 1.18,
        'São Luís': 1.10,
        'Aracaju': 0.79,
        'Campo Grande': 1.02,
        'Goiânia': 0.75,
        'Brasília': 0.22,
        'Belém': 0.88,
        'Fortaleza': 1.35,
        'Recife': 0.66
    },
    'Despesas pessoais': {
        'Rio Branco': 0.54,
        'São Luís': 0.15,
        'Aracaju': 0.64,
        'Campo Grande': 0.54,
        'Goiânia': 0.29,
        'Brasília': 0.64,
        'Belém': 0.56,
        'Fortaleza': 0.43,
        'Recife': 0.54
    },
    'Educação': {
        'Rio Branco': 0.05,
        'São Luís': 0.04,
        'Aracaju': 0.01,
        'Campo Grande': 0.05,
        'Goiânia': 0.01,
        'Brasília': 0.05,
        'Belém': 0.02,
        'Fortaleza': 0.05,
        'Recife': 0.01
    },
    'Comunicação': {
        'Rio Branco': 0.16,
        'São Luís': 1.05,
        'Aracaju': 0.37,
        'Campo Grande': 0.23,
        'Goiânia': 0.24,
        'Brasília': 0.16,
        'Belém': 0.09,
        'Fortaleza': 0.57,
        'Recife': 0.54
    }
}

# Chamar a funçao 
relatorio(dados_ipca)
