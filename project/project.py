import sys
from tabulate import tabulate



def create_game_map(nb: int):
    game_map = [["." for i in range(nb)] for j in range(nb)]
    """ game_map=[]
    row=[]
    for _ in range(nb):
        row.append(".")
    for _ in range(nb):
        game_map.append(row) """
    return game_map


def print_game(game_map):
    print(tabulate(game_map, headers="keys", tablefmt="grid"))


def isFull(game_map):
    if "." not in game_map[0]:
        return True
    return False


def insert_in_column(game_map, row, player):
    for i in reversed(range(len(game_map))):
        if game_map[i][row] == ".":
            game_map[i][row] = player
            return True
    return False


def check_winner(game_map, player):
    if len(game_map) < 4:
        return False
    for i in range(len(game_map)):
        for j in range(len(game_map) - 3):
            tile1 = game_map[i][j]
            tile2 = game_map[i][j + 1]
            tile3 = game_map[i][j + 2]
            tile4 = game_map[i][j + 3]
            if tile1 == tile2 == tile3 == tile4 == player:
                return True

    for i in range(len(game_map)):
        for j in range(len(game_map) - 3):
            tile1 = game_map[j][i]
            tile2 = game_map[j + 1][i]
            tile3 = game_map[j + 2][i]
            tile4 = game_map[j + 3][i]
            if tile1 == tile2 == tile3 == tile4 == player:
                return True

    for i in range(len(game_map) - 3):
        for j in range(len(game_map) - 3):
            tile1 = game_map[j][i]
            tile2 = game_map[j + 1][i + 1]
            tile3 = game_map[j + 2][i + 2]
            tile4 = game_map[j + 3][i + 3]
            if tile1 == tile2 == tile3 == tile4 == player:
                return True

            tile1 = game_map[j][i + 3]
            tile2 = game_map[j + 1][i + 2]
            tile3 = game_map[j + 2][i + 1]
            tile4 = game_map[j + 3][i]
            if tile1 == tile2 == tile3 == tile4 == player:
                return True
    return False


def play(nb: int):
    players = ["X", "O"]
    n = 1
    game_map = create_game_map(nb)
    while not isFull(game_map):
        print_game(game_map)
        if check_winner(game_map, players[n]):
            sys.exit(f"\nPlayer {players[n]} WON")
        n = (n + 1) % 2
        while True:
            try:
                row = int(
                    input(f"Player {players[n]} choose a column or QUIT (Ctrl-d) : ")
                )
                if row >= nb or row < 0:
                    raise ValueError
            except ValueError:
                print("Invalid column number")
                pass
            except EOFError:
                sys.exit(f"\nPlayer {players[n]} LOST")
            else:
                if insert_in_column(game_map, row, players[n]):
                    break
                print("Column is full")

    sys.exit("DRAW")
    
def main():
    try:
        nb = int(input("Size of the game map: "))
        if nb < 1:
            raise ValueError
    except ValueError:
        sys.exit("Not an integer !")
    play(nb)



if __name__ == "__main__":
    main()
