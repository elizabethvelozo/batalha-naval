from interacao import *
from logica import *

print('∗ ~~~ ∗ ~~~~~ ∗ ~~~~~~~ ∗ ~~~~~ ∗ ~~~ ∗')
print('             BATALHA NAVAL             ')
print('∗ ~~~ ∗ ~~~~~ ∗ ~~~~~~~ ∗ ~~~~~ ∗ ~~~ ∗')
print()

jogador_1 = pergunta_nome(1)
jogador_2 = pergunta_nome(2)

frota = define_frota()
total_celulas = qtde_celulas(frota)

tabuleiro_jogador_1 = gera_tabuleiro(frota)
tabuleiro_jogador_2 = gera_tabuleiro(frota)

# Exibição dos tabuleiros originais para teste:
pergunta_exibe_tabuleiro(jogador_1, tabuleiro_jogador_1, \
    jogador_2, tabuleiro_jogador_2)

# PARTIDA
celulas_jogador_1 = total_celulas
celulas_jogador_2 = total_celulas

while True:
    # JOGADOR 1
    tiros_acertados = jogada(jogador_1, tabuleiro_jogador_2, celulas_jogador_2)
    celulas_jogador_2 -= tiros_acertados
    if celulas_jogador_2 == 0:
        vencedor = jogador_1
        break

    # JOGADOR 2
    tiros_acertados = jogada(jogador_2, tabuleiro_jogador_1, celulas_jogador_1)
    celulas_jogador_1 -= tiros_acertados
    if celulas_jogador_1 == 0:
        vencedor = jogador_2
        break

print(f'\nVENCEDOR: {vencedor}')
print(f'\n~~~~~~~~~ Tabuleiro de {jogador_1} ~~~~~~~~~')
exibe_tabuleiro(tabuleiro_jogador_1)
print(f'\n~~~~~~~~~ Tabuleiro de {jogador_2} ~~~~~~~~~')
exibe_tabuleiro(tabuleiro_jogador_2)
print(f'\nFIM DE JOGO')
