
from funcoes import posicao_valida, preenche_frota
from funcoes import posiciona_frota, faz_jogada, afundados, monta_tabuleiros


frota = {}

nomes = ['porta-aviões', 'navio-tanque', 'contratorpedeiro', 'submarino']
tamanhos = [4, 3, 2, 1]
quantidades = [1, 2, 3, 4]

for i in range(4):
    nomenav = nomes[i]
    tamanho = tamanhos[i]
    quantidade = quantidades[i]

    for j in range(quantidade):
        valida = False

        while valida == False:
            print(f'Insira as informações referentes ao navio {nomenav} que possui tamanho {tamanho}')

            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))

            if tamanho == 1:
                orientacao = 'vertical'
            else:
                escolha = int(input('Orientação: [1] Vertical [2] Horizontal '))

                if escolha == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)

            if valida == False:
                print('Esta posição não está válida!')

        frota = preenche_frota(frota, nomenav, linha, coluna, orientacao, tamanho)


frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_jogador = posiciona_frota(frota)
tabuleiro_oponente = posiciona_frota(frota_oponente)

jogadas = []
jogadas_oponente = []
jogando = True

while jogando == True:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    nova = False

    while nova == False:
        linha = int(input('Jogador, qual linha deseja atacar? '))

        while linha < 0 or linha > 9:
            print('Linha inválida!')
            linha = int(input('Jogador, qual linha deseja atacar? '))

        coluna = int(input('Jogador, qual coluna deseja atacar? '))

        while coluna < 0 or coluna > 9:
            print('Coluna inválida!')
            coluna = int(input('Jogador, qual coluna deseja atacar? '))

        posicao = [linha, coluna]

        if posicao in jogadas:
            print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        else:
            jogadas.append(posicao)
            nova = True

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

        quant = afundados(frota_oponente, tabuleiro_oponente)

    if quant == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False

    else:
        nova = False

        while nova == False:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)

            posicao = [linha, coluna]

            if posicao not in jogadas_oponente:
                jogadas_oponente.append(posicao)
                nova = True

        print(f'Seu oponente está atacando na linha {linha} e coluna {coluna}')

        tabuleiro_jogador = faz_jogada(tabuleiro_jogador, linha, coluna)

        quant = afundados(frota, tabuleiro_jogador)

        if quant == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False