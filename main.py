from src.game import Game
from src.chessboard.chessboard import Chessboard


def main():

    print("WELCOME TO CRAZY CHESS")

    c = Chessboard()
    c.move_piece((1,3),(2,3))
    c.display_piece_options((2,3))
    c.move_piece((2,3), (5,3))

if __name__ == "__main__":
    main()
