import copy

# Check if there's a winner
def check_winner(board):
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] != "" and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] != "" and board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]

    if board[0][0] != "" and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != "" and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

# Check if the board is full (for draw)
def is_full(board):
    return all(cell != "" for row in board for cell in row)

# Get all possible moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]

# Minimax algorithm
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 1, None
    elif winner == "X":
        return -1, None
    elif is_full(board):
        return 0, None

    if is_maximizing:
        best_score = float("-inf")
        best_move = None
        for i, j in get_available_moves(board):
            board[i][j] = "O"
            score, _ = minimax(board, False)
            board[i][j] = ""
            if score > best_score:
                best_score = score
                best_move = (i, j)
        return best_score, best_move
    else:
        best_score = float("inf")
        best_move = None
        for i, j in get_available_moves(board):
            board[i][j] = "X"
            score, _ = minimax(board, True)
            board[i][j] = ""
            if score < best_score:
                best_score = score
                best_move = (i, j)
        return best_score, best_move

# Get the best move for AI
def get_best_move(board):
    _, move = minimax(copy.deepcopy(board), True)
    return move
