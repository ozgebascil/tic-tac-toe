X = 'x'
O = 'o'
E = 'e'


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



def run_game():
    print "GAME"


if __name__ == "__main__":
    #run_game()
    print get_input(X)
