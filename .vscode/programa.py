from funcoes import posiciona_frota, faz_jogada, afundados, monta_tabuleiros
from funcoes import posicao_valida, preenche_frota

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

            if nomenav == 'submarino':
                orientacao = 'vertical'
            else:
                escolha = int(input('[1] Vertical [2] Horizontal >'))

                if escolha == 1:
                    orientacao = 'vertical'
                else:
                    orientacao = 'horizontal'

            valida = posicao_valida(frota, linha, coluna, orientacao, tamanho)

            if valida == False:
                print('Esta posição não está válida!')

        frota = preenche_frota(frota, nomenav, linha, coluna, orientacao, tamanho)