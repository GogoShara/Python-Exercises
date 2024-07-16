#JogoDaVelha
print ("Bem vindos ao Jogo da Velha no Python")

def criarBoard():
    return [' ' for _ in range(9)]
def mostrarBoard(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
board= criarBoard()
mostrarBoard(board)

def vencedores(board,player):
    paravencer= [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for combo in paravencer:
        if all(board[i]==player for i in combo):
            return True
    return False

def empate(board):
    return all(cell != ' ' for cell in board)

def movimentosPlayers(player):
    while True:
        try:
            move= int(input(f"Jogador{player}, escolha uma posição de 1 a 9"))- 1
            if move in range(9):
                return move
            else:
                print("Número inválido. Por favor escolha outro número que esteja entre 1 e 9")
        except ValueError:
            print("Input incorreto. Por favor escreva um número")

def jogar():
    board= criarBoard()
    current_player = "X"

    while True:

        mostrarBoard(board)
        move = movimentosPlayers(current_player)

        if board[move]==' ':
            board[move] = current_player
        else:
            print("Casa já ocupada, escolha outro")
            continue

        if vencedores(board, current_player):
            mostrarBoard(board)
            print(f"Jogador {current_player} wins!")
            break
            
        if empate(board):
            mostrarBoard(board)
            print("It's a tie!")
            break

        if current_player=="X":
            current_player="O"
        else:
            current_player="X"

jogar()
   
