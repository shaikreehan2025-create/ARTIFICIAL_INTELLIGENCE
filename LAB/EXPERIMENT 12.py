def print_board(board):
    for i in range(3):
        print(f" {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} ")
        if i < 2:
            print("---+---+---")
    print()

def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def tic_tac_toe():
    board = [' '] * 9
    moves = [(0, 'X'), (4, 'O'), (1, 'X'), (2, 'O'), (3, 'X'), (6, 'O'), (7, 'X')]

    print("Tic Tac Toe Game Simulation (Player X vs Player O):\n")
    print("Initial Empty Board:")
    print_board(board)

    for move, player in moves:
        board[move] = player
        print(f"Player {player} marks cell {move}:")
        print_board(board)

        if check_win(board, player):
            print(f"Player {player} wins the game!")
            return

        if is_board_full(board):
            print("Game ended in a Draw!")
            return

tic_tac_toe()