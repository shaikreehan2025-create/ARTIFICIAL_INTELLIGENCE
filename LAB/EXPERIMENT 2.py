N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()

def is_safe(board, row, col):
    # Check left side of current row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col):
    # Base case: If all queens are placed
    if col >= N:
        return True

    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1  # Place queen

            if solve_n_queens(board, col + 1):
                return True

            board[row][col] = 0  # Backtrack

    return False

# Initialize empty 8x8 board
board = [[0 for _ in range(N)] for _ in range(N)]

print("Solving 8-Queen Problem using Backtracking...\n")
if solve_n_queens(board, 0):
    print("Solution Found (Q = Queen, . = Empty Cell):")
    print_board(board)
else:
    print("No solution exists.")