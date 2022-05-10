from src.chessboard.chessboard import Chessboard

class Player:
    def __init__(self, pseudo, color) -> None:
        self._pseudo = pseudo
        self._color = color

    def __str__(self) -> str:
        return self._pseudo

class Game:
    def __init__(self, player1: str = "BlackPlayer", player2: str = "WhitePlayer") -> None:
        self.player_black = Player(player1, "BLACK")
        self.player_white = Player(player2, "WHITE")
        self.chess_board = Chessboard()

    def play(self):
        game_over: bool = False
        current_player = self.player_black

        while not game_over:

            # Switch between two players
            if current_player == self.player_black:
                current_player = self.player_white
            else:
                current_player = self.player_black

            has_played = False

            print(f"It's {current_player.__str__()}'s turn.\n")

            print(self.chess_board)


            while not has_played:
                try:

                    print("Sélectionner une pièce pour voir les disponibilités :\n")
                    print("\t- ligne, colonne => pour voir les disponibilités d'une pièce")
                    print("\t- ligne, colonne ; ligne, colonne => pour déplacer une pièce")

                    player_input = input(" > ").strip().split(";")
                    values = []

                    for elements in player_input:
                        value = [int(val) for val in elements.split(',')]
                        values.append(value)

                    if self.chess_board.get_piece_at(values[0]).color() == current_player._color:

                        if len(values) == 1:
                            self.chess_board.display_piece_options(*values)
                        elif len(values) == 2:
                            self.chess_board.move_piece(*values)
                            has_played = True
                    else:
                        print("Vous ne pouvez pas manipuler une pièce qui n'est pas de votre couleur.")
                except KeyboardInterrupt:
                    print("\nThe program was ended.")
                    exit(1)
                except:
                    print("Une erreur mais bon...")