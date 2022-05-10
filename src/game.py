from src.chessboard.chessboard import Chessboard

class Player:
    """La classe qui gère les joueurs dans un jeu"""

    def __init__(self, pseudo, color) -> None:
        self._pseudo = pseudo   # Pseudo du joueur
        self._color = color     # Couleur associée au joueur

    def __str__(self) -> str:
        return self._pseudo

class Game:
    def __init__(self, player1: str = "BlackPlayer", player2: str = "WhitePlayer") -> None:
        """On crée deux joueurs ainsi qu'un échiquier."""

        self.player_black = Player(player1, "BLACK")
        self.player_white = Player(player2, "WHITE")
        self.chess_board = Chessboard()

    def play(self):
        game_over: bool = False
        current_player = self.player_black

        # Boucle de jeu
        while not game_over:

            # Gestion du changement des deux joueurs
            if current_player == self.player_black:
                current_player = self.player_white
            else:
                current_player = self.player_black

            has_played = False # Permet de gérer la boucle pour un joueur


            print(f"It's {current_player.__str__()}'s turn.\n")
            print(self.chess_board)

            # Boucle pour un joueur
            while not has_played:
                try:
                    # Affichage instructions
                    print("Sélectionner une pièce pour voir les disponibilités :\n")
                    print("\t- ligne, colonne => pour voir les disponibilités d'une pièce")
                    print("\t- ligne, colonne ; ligne, colonne => pour déplacer une pièce")

                    # Entrée des coordonées par l'utilisateur
                    player_input = input(" > ").strip().split(";")
                    values = []

                    # Interprétation de l'entrée utilisateur
                    for elements in player_input:
                        value = [int(val) for val in elements.split(',')]
                        values.append(value)

                    print(f"Piece {self.chess_board.get_piece_at(*values)} is selected at {self.chess_board.get_spot_at(*values)._coordinates}")

                    # On vérifie que le joueur peut manipuler la pièce
                    if self.chess_board.get_piece_at(values[0]).color() == current_player._color:
                        
                        # Si il n'y a qu'une coordonnée, c'est juste une vérification de possibilités de mouvements
                        if len(values) == 1:
                            self.chess_board.display_piece_options(*values)
                        
                        # Si deux, c'est un mouvements
                        elif len(values) == 2:
                            if self.chess_board.move_piece(*values):
                                has_played = True
                    else:
                        print("Vous ne pouvez pas manipuler une pièce qui n'est pas de votre couleur.")
        
                except KeyboardInterrupt:   # Gestion du Ctrl + C
                    print("\nThe program was ended.")
                    exit(1)
                except:                     # Gestion des autres erreurs
                    print("Une erreur mais bon...")