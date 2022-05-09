from src.game import Game
from src.chessboard.chessboard import Chessboard


def main():

    print("WELCOME TO CRAZY CHESS")

    # Game("Anatole", "Anatole2").play()

    c = Chessboard()
    c.move_piece((0,4),(7,3))
    c.display_piece_options((7,3))


    print(c)

if __name__ == "__main__":
    main()
