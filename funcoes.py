def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []

    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        else:
            posicoes.append([linha, coluna + i])

    return posicoes


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    if nome_navio not in frota:
        frota[nome_navio] = []

    frota[nome_navio].append(posicoes)

    return frota


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in posicoes:
        linha = posicao[0]
        coluna = posicao[1]

        if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
            return False

        for nomenav in frota:
            for navio in frota[nomenav]:
                if posicao in navio:
                    return False

    return True


def posiciona_frota(frota):
    tabuleiro = []

    for i in range(10):
        linha = []

        for j in range(10):
            linha.append(0)

        tabuleiro.append(linha)

    for nomenav in frota:
        for navio in frota[nomenav]:
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                tabuleiro[linha][coluna] = 1

    return tabuleiro


def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro


def afundados(frota, tabuleiro):
    quant = 0

    for nomenav in frota:
        for navio in frota[nomenav]:
            certo = 0

            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]

                if tabuleiro[linha][coluna] == 'X':
                    certo += 1

            if certo == len(navio):
                quant += 1

    return quant


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(10):
        jogador_info = ''
        oponente_info = ''

        for coluna in range(10):
            jogador_info += str(tabuleiro_jogador[linha][coluna])

            valor = tabuleiro_oponente[linha][coluna]

            if valor == 'X' or valor == '-':
                oponente_info += valor
            else:
                oponente_info += '0'

            if coluna < 9:
                jogador_info += '  '
                oponente_info += '  '

        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'

    return texto