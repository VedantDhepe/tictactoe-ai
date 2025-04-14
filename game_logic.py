def check_winner(board):
    # Rows, columns, diagonals
    lines = []

    # Rows and Columns
    for i in range(3):
        lines.append(board[i])  # rows
        lines.append([board[0][i], board[1][i], board[2][i]])  # cols

    # Diagonals
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line[0] and line.count(line[0]) == 3:
            return line[0]
    return None

def is_full(board):
    return all(cell for row in board for cell in row)

# Minimax AI
def get_best_move(board):
    def minimax(board, depth, is_maximizing):
        winner = check_winner(board)
        if winner == "O":
            return 1
        elif winner == "X":
            return -1
        elif is_full(board):
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        score = minimax(board, depth + 1, False)
                        board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        score = minimax(board, depth + 1, True)
                        board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score

    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move
