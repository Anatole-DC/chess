from typing import List, Tuple


class Piece:
    """Base class for a Piece object. Every Piece in the game inherit from this class."""

    def __init__(
        self, name: str = None, stricon: str = None, mvt: List[Tuple[int]] = None
    ):
        self._name: str = name
        self._mvt: List[Tuple[int]] = mvt
        self._stricon: str = stricon
        self._temp_potential_spots = []
        self._temp_potential_targets = []

    def get_available_movements(self, spot, grid: List):
        """Récupère les mouvements possibles pour une pièce."""

        if self._temp_potential_spots != []:
            return self._temp_potential_spots

    def get_targets(self, spot, grid):
        """Récupère les cibles d'une pièce."""

        if self._temp_potential_targets != []:
            return self._temp_potential_targets

    def reset_potential_spots(self):
        """Remet le cache d'une pièce à 0."""
        
        self._temp_potential_spots = []
        self._temp_potential_targets = []
        return self

class PieceNoire(Piece):
    """All Black pieces are inheriting from this class."""

    def color(self):
        return "BLACK"

    def __str__(self) -> str:
        return f"\033[38;2;{0};{0};{255}m{self._stricon}\033[38;2;255;255;255m"


class PieceBlanche(Piece):
    """All White pieces are inheriting from this class."""

    def color(self):
        return "WHITE"

    def __str__(self) -> str:
        return f"\033[38;2;{255};{255};{255}m{self._stricon}\033[38;2;255;255;255m"


class Option(Piece):
    """Option is a spot displayed on the grid."""

    def __init__(self):
        super().__init__("Option", " * ", [])

    def __str__(self) -> str:
        return f"\033[38;2;{0};{255};{0}m{self._stricon}\033[38;2;255;255;255m"


class Interdit(Piece):
    """Option is a spot displayed on the grid."""

    def __init__(self):
        super().__init__("Option", " * ", [])

    def __str__(self) -> str:
        return f"\033[38;2;{255};{0};{0}m{self._stricon}\033[38;2;255;255;255m"