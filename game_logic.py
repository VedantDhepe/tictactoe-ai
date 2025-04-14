def check_winner(board):
    # rows, columns, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    return None

def is_full(board):
    return all(cell != "" for row in board for cell in row)

def minimax(board, is_max):
    winner = check_winner(board)
    if winner == "O": return 1
    elif winner == "X": return -1
    elif is_full(board): return 0

    best = float('-inf') if is_max else float('inf')
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O" if is_max else "X"
                score = minimax(board, not is_max)
                board[i][j] = ""
                best = max(best, score) if is_max else min(best, score)
    return best

def get_best_move(board):
    best_score = float('-inf')
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

