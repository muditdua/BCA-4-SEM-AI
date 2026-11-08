N = 4  # You can change N to 5, 6, etc.

def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        # Check upper left diagonal
        if board[i] == col - (row - i):
            return False

        # Check upper right diagonal
        if board[i] == col + (row - i):
            return False

    return True


def solve(board, row):
    if row == N:
        # A solution is found
        print_board(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1)
            board[row] = -1


def print_board(board):
    for row in range(N):
        for col in range(N):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# Main execution
board = [-1] * N
solve(board, 0)
