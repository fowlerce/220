"""
Name: Christian Fowler
lab9.py

Problem: Tic Tac Toe

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""

def build_board():
    global board
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)

def is_legal(board, position):
    global check_legal
    if str(board[position - 1]).isnumeric() and 0 < position < 10:
        check_legal = True
    else:
        check_legal = False
    return check_legal

def fill_spot(board, position, shape):
    board[position - 1] = shape.strip().lower()
    print_board(board)

def winning_game(board):
    global winner
    if board[0] == board[1] == board[2]:
        winner = True
    elif board[3] == board[4] == board[5]:
        winner = True
    elif board[6] == board[7] == board[8]:
        winner = True
    elif board[0] == board[3] == board[6]:
        winner = True
    elif board[1] == board[4] == board[7]:
        winner = True
    elif board[2] == board[5] == board[8]:
        winner = True
    elif board[0] == board[4] == board[8]:
        winner = True
    elif board[2] == board[4] == board[6]:
        winner = True
    else:
        winner = False
    return winner

def game_over(board):
    global finish
    if not winner:
        finish = False
    for i in range(board[0], board[8]):
        num = str(board[i])
        check_if_num = num.isnumeric()
        if not check_if_num:
            finish = True
        else:
            finish = False
    return finish

def get_winner(board):
    global who_won
    turn_count = 1
    if game_over(board):
        if turn_count % 2 != 0:
            who_won = 'x'
        elif turn_count % 2 == 0:
            who_won = 'o'
        else:
            who_won = 'None'
        return who_won
    turn_count += 1

def play(board):
    while not game_over(board):
        if not winner:
            x_turn = eval(input('x\'s, choose a position:'))
            if check_legal:
                fill_spot(board, x_turn, 'x')
                if not winner:
                    o_turn = eval(input('o\'s, choose a position:'))
                    if is_legal(board, o_turn):
                        fill_spot(board, o_turn, 'o')

def main():
    pass

if __name__ == '__main__':
    main()
