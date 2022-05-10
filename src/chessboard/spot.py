from typing import List, Tuple

from src.pieces.colored_pieces import *
from src.pieces.piece import Piece, Option

_SPOT_WIDTH: int = 3


class Spot:
    """Classe qui gère les emplacements sur un échiquier."""
    
    def __init__(self, coordinates: Tuple[int], piece: Piece = None) -> None:
        self._coordinates = coordinates # coordonner de l'enplacement sur la grille pour les future deplacement ( ex (0.0))
        self._piece = piece # piece presente sur l'emplacement associer a la coordonner 

    def is_empty(self):
        """nous dis si l'emplecement est libre """
        return self._piece is None

    def empty(self):
        """ empty est la fct qui nous permet de vider les emplacements ( ex pour le deplacement d'un pions on vide la caz preseda&nte ou pour manger ) """    
        self._piece = None
        return self
    
    def place(self, piece: Piece):
        """placer une piece sur l'emplacement precis

        Args:
            piece (Piece): piece à placer

        """
        self._piece = piece
        return self

    def __str__(self) -> str:
        if self.is_empty():
            return " " * _SPOT_WIDTH
        else:
            return self._piece.__str__()
#pour pouvoir print un spot 