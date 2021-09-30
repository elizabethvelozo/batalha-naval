ordem = 10

def pergunta_nome(jogador):
    nome_jogador = input(f'Jogador {jogador}: ')
    nome_jogador = nome_jogador.capitalize()

    return nome_jogador

def pergunta_qtde_navios(tipo_navio, qtde_minima, qtde_maxima):
    while True:
        qtde_navios = input(f'{tipo_navio.capitalize()}[{qtde_minima}-{qtde_maxima}]: ')
        if not qtde_navios.isnumeric():
            print('Insira um valor numérico.')
            continue

        qtde_navios = int(qtde_navios)
        if qtde_navios < qtde_minima or qtde_navios > qtde_maxima:
            print(f'Insira de {qtde_minima} a {qtde_maxima} {tipo_navio} no máximo.')
            continue
        else:
            return qtde_navios

def define_frota():
    ''' Permite ao usuário escolher jogar ou não com frota máxima. Caso não,
    chama a função "pergunta_qtde_navios".
    Retorna o vetor "lista_frota", de três elementos, com a quantidade de cada
    tipo de navio. '''

    lista_frota = [None] * 3

    frota_maxima = input('\nDeseja jogar com frota máxima [S/N]? ')
    frota_maxima = frota_maxima.upper()

    if frota_maxima == 'S':
        for i in range(3):
            lista_frota[i] = i + 1 # quantidade máxima para cada navio
    else:
        print('Digite a quantidade para cada tipo de navio: ')
        lista_frota[0] = pergunta_qtde_navios('porta-aviões', 0, 1)
        lista_frota[1] = pergunta_qtde_navios('cruzadores', 0, 2)
        lista_frota[2] = pergunta_qtde_navios('submarinos', 1, 3)

    return lista_frota

def exibe_tabuleiro(tabuleiro):
    print(f'\n      0  1  2  3  4  5  6  7  8  9')
    for linha in range(ordem):
        print(f'   {chr(linha + 65):3}', end='')
        for coluna in range(ordem):
            print(f'{tabuleiro[linha][coluna]:3}', end='')
        print()

def pergunta_exibe_tabuleiro(nome_jogador_1, tabuleiro_1, nome_jogador_2, tabuleiro_2):
    resposta = input('\nDeseja exibir tabuleiros para teste \n[S/N]? ')
    resposta = resposta.upper()

    if resposta == 'S':
        print(f'\n~~~~~~~~~ Tabuleiro de {nome_jogador_1} ~~~~~~~~~')
        exibe_tabuleiro(tabuleiro_1)
        print(f'\n~~~~~~~~~ Tabuleiro de {nome_jogador_1} ~~~~~~~~~')
        exibe_tabuleiro(tabuleiro_2)

def gera_espelho_tabuleiro(tabuleiro):
    ''' Mascara o tabuleiro do oponente para o jogador e ao longo da partida
    exibe as coordenadas já escolhidas do tabuleiro original. '''

    espelho_tabuleiro = [[None] * ordem for i in range(ordem)]

    for linha in range(ordem):
        for coluna in range(ordem):
            if tabuleiro[linha][coluna] != 'P' and tabuleiro[linha][coluna] != 'C' \
             and tabuleiro[linha][coluna] != 'S' and tabuleiro[linha][coluna] != '∗':
                espelho_tabuleiro[linha][coluna] = '□'
            else:
                espelho_tabuleiro[linha][coluna] = tabuleiro[linha][coluna]

    return espelho_tabuleiro

def pergunta_coordenadas():
    ''' Permite ao usuário inserir as coordenadas num único input, separando-as
    com tratamento de string. Faz validações para que não seja possível
    a escolha de coordenadas inexistentes.
    Retorna o vetor "coordenadas", de dois elementos. '''

    while True:
        coordenadas = input('\nEscolha as coordenadas [A-J][0-9]: ')
        if len(coordenadas) != 2:
            print('São necessárias duas coordenadas.')
            continue

        coordenada_1 = coordenadas[0]
        coordenada_2 = coordenadas[1]
        if not coordenada_1.isalpha() or not coordenada_2.isnumeric():
            print('Insira as coordenadas no formato \n[letra][número].')
            print('Exemplo: A0')
            continue

        coordenada_1 = ord(coordenada_1.upper()) - 65
        coordenada_2 = int(coordenada_2)
        if coordenada_1 > 9:
            print('Insira uma coordenada de A a J \ne outra de 0 a 9.')
            continue

        coordenadas = [None] * 2
        for i in range(2):
            coordenadas[0] = coordenada_1
            coordenadas[1] = coordenada_2

        return coordenadas