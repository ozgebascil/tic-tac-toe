X = 'X'
O = 'O'
E = '_'
X_WIN = 0
O_WIN = 1
DRAW = 2
CONTINUE = 3


def get_input(symbol):
    coord = raw_input("Please enter coordinates for %s in the following format 1 2  : " % symbol)
    coord = coord.split()

    if len(coord) != 2:
        print "INVALID INPUT!"
        return get_input(symbol)

    x, y = coord

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        print "INVALID INPUT!"
        return get_input(symbol)

    if not(x in [0, 1, 2] and y in [0, 1, 2]):
        print "INVALID INPUT!"
        return get_input(symbol)

    return x, y


def update_board(symbol, x, y, board):

    if board[x][y] == E:
        board[x][y] = symbol
        return board
    raise ValueError


def print_board(board):

    for row in board:
        print " ".join(row)


def check_board(board):
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]
    columns = []
    for i in range(3):
        column = [row[i] for row in board]
        columns.append(column)

    lst = board + columns + [diag1, diag2]

    if [X, X, X] in lst:
        return X_WIN
    elif [O, O, O] in lst:
        return O_WIN


def run_game():
    print "GAME"


if __name__ == "__main__":
    #run_game()
    #print update_board(X, 0, 0, [[X, E, O], [E, E, E], [O, E, X]])
    #print_board([[X, E, O], [E, E, E], [O, E, X]])
    print check_board([[X, E, O], [X, E, O], [E, E, O]])
