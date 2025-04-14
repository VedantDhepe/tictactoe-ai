import streamlit as st
from game_logic import check_winner, is_full, get_best_move

# Page config
st.set_page_config(page_title="Tic-Tac-Toe AI", layout="wide")

# Custom styling for mobile responsiveness
st.markdown("""
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
    .game-wrapper {
        max-width: 400px;
        margin: auto;
    }
    button[kind="secondary"] {
        height: 70px !important;
        font-size: 24px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 Tic-Tac-Toe with AI (Minimax)")

# Initialize game state
if "board" not in st.session_state:
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "turn" not in st.session_state:
    st.session_state.turn = "X"
if "game_started" not in st.session_state:
    st.session_state.game_started = False

# --- Game logic ---
def player_move(i, j):
    if st.session_state.board[i][j] == "" and not st.session_state.game_over and st.session_state.turn == "X":
        st.session_state.board[i][j] = "X"
        winner = check_winner(st.session_state.board)
        if winner or is_full(st.session_state.board):
            st.session_state.game_over = True
        else:
            st.session_state.turn = "O"
            ai_move()

def ai_move():
    move = get_best_move(st.session_state.board)
    if move:
        st.session_state.board[move[0]][move[1]] = "O"
    winner = check_winner(st.session_state.board)
    if winner or is_full(st.session_state.board):
        st.session_state.game_over = True
    else:
        st.session_state.turn = "X"

def reset_game():
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.turn = "X"
    st.session_state.game_over = False
    st.session_state.game_started = False

# --- Game UI ---
if not st.session_state.game_started:
    if st.button("🎮 Start Game", use_container_width=True):
        st.session_state.game_started = True
        reset_game()
else:
    st.markdown("<div class='game-wrapper'>", unsafe_allow_html=True)

    for i in range(3):
        cols = st.columns([1, 1, 1])
        for j in range(3):
            label = st.session_state.board[i][j] or " "
            cols[j].button(
                label,
                key=f"{i}-{j}",
                on_click=player_move,
                args=(i, j),
                use_container_width=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

    winner = check_winner(st.session_state.board)
    if winner:
        st.success(f"🎉 Winner: {winner}")
    elif is_full(st.session_state.board):
        st.info("It's a draw!")

    st.button("🔄 Reset Game", on_click=reset_game, use_container_width=True)
