def inserir_ordenado(lista, x):
    i = 0  # Começa do início da lista
    # Avança enquanto o elemento atual for menor que x
    while i < len(lista) and lista[i] < x:
        i += 1
    # Insere x na posição correta para manter a ordem crescente
    lista.insert(i, x)
#-------------------------------------------
def contar_frases(texto):
    i = 0              # Índice para percorrer o texto
    frases = 0         # Contador de frases encontradas
    while i < len(texto):
        # Verifica se o caractere é pontuação final de frase
        if texto[i] in '.!?':
            # Verifica se são reticências
            if texto[i:i+3] == '...':
                frases += 1  # Conta como uma frase
                i += 3       # Pula os três pontos
            else:
                frases += 1  # Conta pontuação simples como frase
                i += 1
        else:
            i += 1  # Continua percorrendo
    return frases
#-----------------------------------------------
import random

def lancar_dado(n):
    # Cria dicionário com contagem inicial 0 para as 6 faces
    frequencia = {i: 0 for i in range(1, 7)}
    
    for _ in range(n):  # Repete n vezes
        face = random.randint(1, 6)  # Sorteia face de 1 a 6
        frequencia[face] += 1        # Incrementa a contagem daquela face
        
    return frequencia  # Retorna dicionário com frequência de cada face
#-----------------------------
def contar_palavras_v2(frase):
    i = 0
    # Remove espaços à esquerda
    while frase[i] == ' ':
        i = i + 1

    j = len(frase) - 1
    # Remove espaços à direita
    while frase[j] == ' ':
        j = j - 1

    espacos = 0
    # Conta quantos espaços existem entre i e j
    for k in range(i, j+1):
        if frase[k] == ' ':
            espacos += 1

    return espacos + 1  # Número de palavras = espaços + 1

#------------------------------------
def contar_palavras(frase):
    # Divide a frase em palavras, ignorando múltiplos espaços e espaços nas bordas
    palavras = frase.split()
    return len(palavras)  # Retorna o número de palavras encontradas

#-----------------------

import random

def gerar_numeros_aleatorios_diferentes(n):
    if n > 101:
        raise ValueError("Não é possível gerar mais de 101 números diferentes entre 0 e 100")
    
    # Usa sample para gerar n valores únicos entre 0 e 100
    return random.sample(range(101), n)

#------------/----------

def contar_frases(texto):
    return texto.count('.') + texto.count('!') + texto.count('?') - texto.count('...')
