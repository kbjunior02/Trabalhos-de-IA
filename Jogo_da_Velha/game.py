from random import randint

# VARIÁVEIS GLOBAIS
dim = 3             # Dimenção do tabuleiro
computador = 'x'    # Simbolo para o computador (1)
humano = 'o'        # Simbolo do jogador humano (-1)
vazio = ' '         # Simbolo para espaço não jogado
player = -1         # Jogador atual (padrão: inicia com humano: -1)
infinito = 111000   # Valor infinito utilizado
tab = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']] # Tabuleiro 3x3
depth = dim**2      # Profundidade inicial - Tabuleiro vazio

# Retorna 1 se player = X ou -1 para player = O e 0 caso contrário
def player_to_int(player = '') -> int:
    return 1 if player == computador else (-1 if player == humano else 0)

# Retorna X se player = 1 ou O para player = -1 e '' caso contrário
def player_to_char(player = 0) -> str:
    return computador if player == 1 else (humano if player == -1 else vazio)

# Retorna 1 se X ganhou, -1 se 0 ganhou, 0 caso contrário.
def custo(tabuleiro) -> int:
    for i in range(dim): # Checagem das linhas e colunas
        if(tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != vazio):
            return player_to_int(tabuleiro[i][0])
        if(tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != vazio):
            return player_to_int(tabuleiro[0][i])

    if(tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != vazio):
        return player_to_int(tabuleiro[0][0])
    if(tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] != vazio):
        return player_to_int(tabuleiro[1][1])
    return 0

# Retorna o tabuleiro que resulta ao fazer a jogada i,j
def resultado(tabuleiro, acao):
    x, y = acao[0], acao[1]
    if tabuleiro[x][y] == vazio:
        tabuleiro[x][y] = player_to_char(player)
        return tabuleiro
    else:
        print("Jogada não permitida! Campo já preenchido.")
        return None
    
# Retorna o ganhador, se houver
def ganhador(tabuleiro) -> str:
    r = player_to_char(custo(tabuleiro))
    return r if r != vazio else "Empate"

# Retorna Verdadeiro se o jogo acabou, Falso caso contrário
def final(tabuleiro) -> bool:
    return True if custo(tabuleiro) != 0 or len(acoes(tabuleiro)) == 0 else False

# Retorna todas as jogadas disponíveis
def acoes(tabuleiro):
    jogadas = []
    for i in range(dim):
        for j in range(dim):
            if tabuleiro[i][j] == vazio:
                jogadas.append([i,j])
    return jogadas

# Retorna a jogada ótima para o jogador atual
def minimax(tabuleiro, profundidade, p):

    if p == player_to_int(computador): # Caso o player seja o computador
        best = [-1, -1, -infinito]     # Define a busca pelo valor máximo
    else:
        best = [-1, -1, +infinito]     # Define a busca pelo valor mínimo

    if profundidade == 0 or final(tabuleiro): # Caso folha da arvore de recursão
        score = custo(tabuleiro)
        return [-1, -1, score] # Retorna somente pontuação

    for acao in acoes(tabuleiro):
        x, y = acao[0], acao[1]
        tabuleiro[x][y] = player_to_char(p)
        score = minimax(tabuleiro, profundidade - 1, -p)
        tabuleiro[x][y] = player_to_char(0)
        score[0], score[1] = x, y

        if p == player_to_int(computador):
            if score[2] > best[2]:
                best = score  # max value
        else:
            if score[2] < best[2]:
                best = score  # min value
    return best

def exibir_tabluleiro(tab, dim):
    print("-"*13)
    for i in range(dim):
        print('| ' + tab[i][0] + ' | ' + tab[i][1] + ' | ' + tab[i][2] + ' |')
        print("-"*13)

if __name__ == "__main__":

    # Seleciona o jogador aleatoriamente, padrão será o humano iniciar
    # player = -1 if randint(0,1) == 0 else 1 

    while True:
        exibir_tabluleiro(tab,dim)

        if final(tab): break

        if player == -1:
            x, y = input("Digite sua jogada (x,y): ").split()
            x = int(x)
            y = int(y)
            if (x < 3 and x >= 0) and (y < 3 and y >= 0) and tab[x][y] == vazio:
                tab = resultado(tab, [x, y])
                player = -player
                depth -= 1
            else:
                print("Jogada não permitida. Tente novamente...")
        else:
            print("Jogada do computador: ", end="")
            acao_computador = minimax(tab, depth, player)
            tab = resultado(tab, acao_computador)
            print(acao_computador[0], acao_computador[1])
            player = -player
            depth -= 1

    print("Vencedor: ", ganhador(tab))
