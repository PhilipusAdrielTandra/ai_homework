import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']

def minimax(board, depth, is_maximizing):
    scores = {'X': 1, 'O': -1, 'Tie': 0}

    if is_winner(board, 'X'):
        return scores['X']
    if is_winner(board, 'O'):
        return scores['O']
    if is_draw(board):
        return scores['Tie']

    if is_maximizing:
        best_score = -float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'X'
            score = minimax(board, depth + 1, False)
            board[i][j] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i, j in get_empty_cells(board):
            board[i][j] = 'O'
            score = minimax(board, depth + 1, True)
            board[i][j] = ' '
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = (-1, -1)
    for i, j in get_empty_cells(board):
        board[i][j] = 'X'
        score = minimax(board, 0, False)
        board[i][j] = ' '
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)
    ]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player_i, player_j = map(int, input("Enter your move (row and column, e.g., 0 0): ").split())
        if board[player_i][player_j] == ' ':
            board[player_i][player_j] = 'O'
        else:
            print("Invalid move. Try again.")
            continue

        if is_winner(board, 'O'):
            print_board(board)
            print("You win!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)
        print("Bot is thinking...")
        bot_i, bot_j = best_move(board)
        board[bot_i][bot_j] = 'X'

        if is_winner(board, 'X'):
            print_board(board)
            print("Bot wins!")
            break

        if is_draw(board):
            print_board(board)
            print("It's a tie!")
            break

        print_board(board)

main()