from random import randint
from interacao import *

ordem = 10

def qtde_celulas(lista_frota):
    total_celulas = (lista_frota[0] * 4) + (lista_frota[1] * 3) + (lista_frota[2] * 2)

    return total_celulas

def gera_posicao(direcao, celulas_navio):
    ''' Posição aleatória que será usada como referência para alocar um navio.
    No randint, o parâmetro "celulas_navio" é subtraído da "ordem" para que um
    navio sempre seja alocado dentro do intervalo do tabuleiro.
    Retorna um vetor de dois elementos, os quais representam, consecutivamente
    linha e coluna. '''

    posicao = [None] * 2

    if direcao == 0:
        finda_randint_linha = ordem -  1
        finda_randint_coluna = ordem - celulas_navio
    else:
        finda_randint_linha = ordem - celulas_navio
        finda_randint_coluna = ordem - 1

    posicao[0] = randint(0, finda_randint_linha)
    posicao[1] = randint(0, finda_randint_coluna)

    return posicao

def checa_posicao_valida(posicao, direcao, tabuleiro, celulas_navio):
    ''' Checa as posições vizinhas e também as que estaria alocado um navio.
    Ignora posições fora do intervalo do tabuleiro com o "continue".
    Retorna um valor booleano que representa se a posição é válida ou não. '''

    linha = posicao[0]
    coluna = posicao[1]

    if direcao == 0:
        finda_linha = linha + 2
        finda_coluna = coluna + celulas_navio + 1
    else:
        finda_linha = linha + celulas_navio + 1
        finda_coluna = coluna + 2

    for i in range(linha - 1, finda_linha):
        if i < 0 or i > 9:
            continue
        for j in range(coluna - 1, finda_coluna):
            if j < 0 or j > 9:
                continue
            if tabuleiro[i][j] == 'p' or tabuleiro[i][j] == 'c' or tabuleiro[i][j] == 's':
                return False

    return True

def aloca_navio(posicao, direcao, celulas_navio, tabuleiro, tipo_navio):
    ''' Feita a validação, a posição gerada e também, de acordo com a extensão
    de cada tipo de navio, as próximas posições em fileira são preenchidas
    com a letra que representa determinado navio. '''

    linha = posicao[0]
    coluna = posicao[1]

    if direcao == 0:
        for j in range(coluna, coluna + celulas_navio):
            tabuleiro[linha][j] = tipo_navio
    else:
        for j in range(linha, linha + celulas_navio):
            tabuleiro[j][coluna] = tipo_navio

def gera_tabuleiro(lista_frota):
    tabuleiro = [['□'] * ordem for i in range(ordem)]
    tipos_navio = ['p', 'c', 's']

    for i in range(3):
        qtde_navios = lista_frota[i]
        tipo_navio = tipos_navio[i]
        celulas_navio = 4 - i

        while qtde_navios > 0:
            direcao = randint(0, 1)

            posicao = gera_posicao(direcao, celulas_navio)
            posicao_valida = checa_posicao_valida(posicao, direcao, tabuleiro, celulas_navio)
            if posicao_valida:
                aloca_navio(posicao, direcao, celulas_navio, tabuleiro, tipo_navio)

                qtde_navios -= 1

    return tabuleiro

def verifica_coordenadas(coordenadas, tabuleiro_oponente):
    if tabuleiro_oponente[coordenadas[0]][coordenadas[1]] == 'p':
        resultado = 'FOGO'
        tabuleiro_oponente[coordenadas[0]][coordenadas[1]] = 'P'
    elif tabuleiro_oponente[coordenadas[0]][coordenadas[1]] == 'c':
        resultado = 'FOGO'
        tabuleiro_oponente[coordenadas[0]][coordenadas[1]] = 'C'
    elif tabuleiro_oponente[coordenadas[0]][coordenadas[1]] == 's':
        resultado = 'FOGO'
        tabuleiro_oponente[coordenadas[0]][coordenadas[1]] = 'S'
    elif tabuleiro_oponente[coordenadas[0]][coordenadas[1]] == '□':
        resultado = 'ÁGUA'
        tabuleiro_oponente[coordenadas[0]][coordenadas[1]] = '∗'
    else:
        resultado = 'ERRO'

    return resultado

def jogada(nome_jogador, tabuleiro_oponente, celulas_oponente):
    tiros_acertados = 0
    while True:
        print(f'\n~~~~~~~~~~~~ Vez de {nome_jogador} ~~~~~~~~~~~~')
        exibe_tabuleiro(gera_espelho_tabuleiro(tabuleiro_oponente))
        coordenadas = pergunta_coordenadas()
        resultado = verifica_coordenadas(coordenadas, tabuleiro_oponente)

        print(f'{resultado}!')
        if resultado == 'FOGO':
            print('Você acertou o tiro.')
            tiros_acertados += 1
            if tiros_acertados == celulas_oponente:
                return tiros_acertados
        elif resultado == 'ERRO':
            print('Essa coordenada já foi escolhida.')
            continue
        else:
            print('Você errou o tiro.')
            return tiros_acertados