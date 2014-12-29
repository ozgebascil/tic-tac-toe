X = 'X'
O = 'O'
E = '_'


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



def run_game():
    print "GAME"


if __name__ == "__main__":
    #run_game()
    print update_board(X, 0, 0, [[X, E, O], [E, E, E], [O, E, X]])
    #print_board([[X, E, O], [E, E, E], [O, E, X]])
