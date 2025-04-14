import streamlit as st
from game_logic import check_winner, is_full, get_best_move

st.set_page_config(page_title="Tic-Tac-Toe AI", layout="centered")
st.title("🤖 Tic-Tac-Toe with AI (Minimax) --------------   (Double tap on a cell )")

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "turn" not in st.session_state:
    st.session_state.turn = "X"  # Human starts

# Function to handle player move
def player_move(i, j):
    if st.session_state.board[i][j] == "" and not st.session_state.game_over and st.session_state.turn == "X":
        st.session_state.board[i][j] = "X"
        winner = check_winner(st.session_state.board)
        if winner or is_full(st.session_state.board):
            st.session_state.game_over = True
            return
        st.session_state.turn = "O"

# Function to handle AI move
def ai_move():
    move = get_best_move(st.session_state.board)
    if move:
        st.session_state.board[move[0]][move[1]] = "O"
    winner = check_winner(st.session_state.board)
    if winner or is_full(st.session_state.board):
        st.session_state.game_over = True
    st.session_state.turn = "X"

# Track which cell is clicked
clicked_cell = None

# Display the game grid
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        button_label = st.session_state.board[i][j] or " "
        if cols[j].button(button_label, key=f"{i}-{j}"):
            clicked_cell = (i, j)

# Handle player move
if clicked_cell:
    i, j = clicked_cell
    player_move(i, j)

# Handle AI move
if st.session_state.turn == "O" and not st.session_state.game_over:
    ai_move()

# Display game result
winner = check_winner(st.session_state.board)
if winner:
    st.success(f"🎉 Winner: {winner}")
elif is_full(st.session_state.board):
    st.info("It's a draw!")

# Reset game
if st.button("🔄 Reset Game"):
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.game_over = False
    st.session_state.turn = "X"
