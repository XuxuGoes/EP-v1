def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    
    for i in range(tamanho):
        if orientacao == "vertical":
            posicoes.append([linha + i, coluna])
        if orientacao == "horizontal":
            posicoes.append([linha, coluna + i])
            
    return posicoes

# Exemplo de uso conforme o enunciado
# linha = 2
# coluna = 4
# orientacao = "vertical"
# tamanho = 3

# print(define_posicoes(linha, coluna, orientacao, tamanho))