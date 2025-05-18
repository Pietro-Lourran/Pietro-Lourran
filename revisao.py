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