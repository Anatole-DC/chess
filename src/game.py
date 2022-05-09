from src.chessboard.chessboard import Chessboard

class Player:
    def __init__(self, pseudo, color) -> None:
        self._pseudo = pseudo
        self._color = color

class Game:
    def __init__(self, player1: str = "BlackPlayer", player2: str = "WhitePlayer") -> None:
        self.player_black = Player(player1, "BLACK")
        self.player_white = Player(player2, "WHITE")
        self.chess_board = Chessboard()

    def play(self):
        game_over: bool = False
        current_player = self.player_white

        while not game_over:

            # Switch between two players
            if current_player == self.player_black:
                current_player = self.player_white
            else:
                current_player = self.player_black

            print(f"It's {current_player}'s turn.")

            print(self.chess_board)

            piece = tuple(int(element) for element in input("Selectionner un jeton : \n").strip().split(","))
            while len(piece) != 2:
                print("Input must be in format line, column")
                piece = tuple(int(element) for element in input("Selectionner un jeton : \n").strip().split(","))

            if self.chess_board.chess_mate():
                game_over = True