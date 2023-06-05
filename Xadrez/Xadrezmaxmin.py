import chess
from math import inf



def alphabeta(no,tab, profundidade, alpha, beta, maximizacao):
    if tab.is_checkmate():  # Analisa de a jogada está em checkmate
        return (-40 if maximizacao else 40)
    elif tab.is_game_over():  # Verifica se o jogo acabou devido a checkmate
        return 0

    if profundidade == 0 or no == 0 :  # Verifica se a profundidade é zero, caso seja, retorna o tabuleiro
        return valorBorda(tab)

    if maximizacao:  # Caso maximize for True, entra nessa codição
        melhorValor = - inf  # . Caso for o turno do oponente, o algoritmo guarda o menor (Min) resultado de suas respectivas ramificações.
        for movimento in tab.legal_moves: # Se o movimento for válido, copiamos o tabuleiro
            tabuleiroExp = tab.copy()
            tabuleiroExp.push(movimento)  # Aqui analisamos a movimentação da jogada
            valor = max(melhorValor, (alphabeta(no,tabuleiroExp, profundidade, alpha, beta, False)))
            melhorValor = max(melhorValor, valor)
            alpha = max(alpha, melhorValor)
            if(alpha >= beta):
                break

        return melhorValor
    else:
        melhorValor = inf  # Caso for o turno do jogador, o algoritmo guarda o maior(max) resultado das suas respectivas ramificações
        for movimento in tab.legal_moves:
            tabuleiroExp = tab.copy()
            tabuleiroExp.push(movimento)
            valor = min(melhorValor, (alphabeta(no,tabuleiroExp, profundidade - 1,alpha, beta, True)))
            melhorValor = min(melhorValor, valor)
            beta = min(beta, melhorValor)
            if alpha >= beta:
                break
        return melhorValor




def valorBorda(borda):
    bordaString = borda.fen().split()[0]  # O FEN para a posição de partida padrão do xadrez.
    peaoDiff = bordaString.count("P") - bordaString.count("p")
    torreDiff = bordaString.count("R") - bordaString.count("r")
    cavaloDiff = bordaString.count("N") - bordaString.count("n")
    bispoDiff = bordaString.count("B") - bordaString.count("b")
    rainhaDiff = bordaString.count("Q") - bordaString.count("q")

    return 1 * peaoDiff + 3 * bispoDiff + 3 * cavaloDiff + 5 * torreDiff + 9 * rainhaDiff  # cada número que multiplica a var representa o tipo da paça
    # Por exemplo: chess.pawn = 1


if __name__ == "__main__":
    tabuleiro = chess.Board()  # Cria o tabuleiro com todas as peças

    while True:

        print(tabuleiro)
        print(tabuleiro.legal_moves)  # Imprime as opções de jogadas a serem feitas. Paramêtro concecida do chess
        movimentoUsuario = input("Digite o movimento que deseja criar: ")
        tabuleiro.push_san(movimentoUsuario)  # Responsável pela movimentação da jogada

        if tabuleiro.is_checkmate():  # Verifica se a posição atual é um xeque mate.
            print(tabuleiro)
            print("Usuário vence!")
            break
        elif tabuleiro.is_game_over():  # Verifica se o jogo acabou devido a checkmate, stalemate, , o , ou um .insufficient materialseventyfive-move rulefivefold repetitionvariant end condition
            print(tabuleiro)
            print("Jogo Empate")
            break

        minValor = inf
        minMovimento = None
        for movimento in tabuleiro.legal_moves:
            tabuleiroExp = tabuleiro.copy()
            tabuleiroExp.push(movimento)
            valor = alphabeta(0,tabuleiroExp, 4, - inf, inf, False)

            if valor < minValor:
                minValor = valor
                minMovimento = movimento

        tabuleiro.push(minMovimento)
        if tabuleiro.is_checkmate():
            print(tabuleiro)
            print("Computador vence!")
            break
        elif tabuleiro.is_game_over():
            print(tabuleiro)
            print("Jogo Empate")
            break
