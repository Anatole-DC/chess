from typing import List, Tuple


class Piece:
    """Base class for a Piece object. Every Piece in the game inherit from this class."""

    def __init__(
        self, name: str = None, stricon: str = None, mvt: List[Tuple[int]] = None
    ):
        self._name: str = name
        self._mvt: List[Tuple[int]] = mvt
        self._stricon: str = stricon

    def get_available_movements(self, spot, grid):
        pass

class BlackPiece(Piece):
    """All Black pieces are inheriting from this class."""

    def color(self):
        return "BLACK"

    def __str__(self) -> str:
        return f"\033[38;2;{0};{0};{255}m{self._stricon}\033[38;2;255;255;255m"


class WhitePiece(Piece):
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