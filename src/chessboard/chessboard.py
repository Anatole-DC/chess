from typing import List, Tuple

from src.chessboard.spot import Spot, _SPOT_WIDTH
from src.pieces.colored_pieces import *
from src.pieces.piece import Piece, Option



class Chessboard:
    def __init__(self):

        # initialisation de la grille 
        self._grid: List[List[Spot]] = []
        for i in range(8):
            line: List[Spot] = []
            for j in range(8):
                line.append(Spot((i, j)))
            self._grid.append(line)

        # Init ligne pions
        [spot.place(BlackPawn()) for spot in self._grid[1]]
        [spot.place(WhitePawn()) for spot in self._grid[6]]

        # Init les autres 
        black_majors: List[Piece] = [BlackRook(), BlackKnight(), BlackBishop(), BlackKing(), BlackQueen(), BlackBishop(), BlackKnight(), BlackRook()]
        white_majors: List[Piece] = [WhiteRook(), WhiteKnight(), WhiteBishop(), WhiteQueen(), WhiteKing(), WhiteBishop(), WhiteKnight(), WhiteRook()]

        for i in range(8):
            self._grid[0][i].place(black_majors[i])
            self._grid[7][i].place(white_majors[i])

        self.dead_pieces: List[Piece] = []

    def get_spot_at(self, coordinates: Tuple[int]) -> Spot:
        """recuperer un spot quand on donne des coordonner 

        Args:
            coordinates (Tuple[int]): The coordinates (line, column).

        Returns:
            Spot: The Spot.
        """

        return self._grid[coordinates[0]][coordinates[1]]

    def get_piece_at(self, coordinates: Tuple[int]) -> Piece:
        """Fetch a piece at the position given.

        Args:
            coordinates (Tuple[int]): The coordinates at which we want to fetch the piece.

        Returns:
            Piece: The Piece returned.
        """

        return self.get_spot_at(coordinates)._piece


    def move_piece(self, from_spot: Tuple[int], to_spot: Tuple[int]):
        """Move a piece to a different spot

        Args:
            from_spot (Tuple[int]): The coordinates of the spot whose piece must be moved.
            to_spot (Tuple[int]): The spot to which the piece is beeing moved.

        Returns:
            Chessboard: The updated chessboard.
        """
        
        to_spot: Spot = self.get_spot_at(to_spot)
        
        if not to_spot.is_empty():
            self.dead_pieces.append(to_spot._piece)
#ajouter a la liste la piece morte
        to_spot.place(self.get_spot_at(from_spot)._piece)
# placer la piece en deplacement sur le spot voulu 
        self.get_spot_at(from_spot).empty()
# on vide l'emplacment de ou est partie le pions 
        return self


    def get_spot_movements(self, spot: Spot):
        return spot._piece.get_available_movements(spot, self._grid)
# recupere les mouvements disponible pour les pieces  
    def display_piece_options(self, coordinates: Tuple[int]) -> None:
        selected_spot: Spot = self.get_spot_at(coordinates)
        temp_grid: Chessboard = Chessboard()
        temp_grid._grid = self._grid
        temp_grid.dead_pieces = self.dead_pieces


        if not selected_spot.is_empty():
        
            movements: List[Spot] = self.get_spot_movements(selected_spot)

            for spot in movements:
                temp_grid.get_spot_at(spot._coordinates)._piece = spot._piece

        print(temp_grid)

    def chess_mate(self) -> bool:
        pass

    def chess(self) -> bool:
        pass

    def __str__(self) -> str:
        str_echiquier: str = f"|{'-'*_SPOT_WIDTH}" * 8 + "|\n"

        for col in self._grid:
            str_echiquier += "|"
            for element in col:
                str_echiquier += f"{element}|"
            str_echiquier += "\n"
            str_echiquier += f"|{'-'*_SPOT_WIDTH}" * 8 + "|\n"

        str_echiquier += "\n"*2

        str_echiquier += "Dead pieces :  ["
        for piece in self.dead_pieces:
            str_echiquier += f" {piece}"
        str_echiquier += " ]\n\n"

        return str_echiquier
