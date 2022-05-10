from src.pieces.chess_pieces import *
from src.pieces.piece import PieceNoire, PieceBlanche


"""
    On crée pour chaque pièce sur l'échiquier une pièce de chaque couleur.
"""

class BlackPawn(Pion, PieceNoire):
    pass


class WhitePawn(Pion, PieceBlanche):
    pass


class BlackRook(Tour, PieceNoire):
    pass


class WhiteRook(Tour, PieceBlanche):
    pass


class BlackKnight(Cavalier, PieceNoire):
    pass


class WhiteKnight(Cavalier, PieceBlanche):
    pass


class BlackBishop(Fou, PieceNoire):
    pass


class WhiteBishop(Fou, PieceBlanche):
    pass


class BlackQueen(Reine, PieceNoire):
    pass


class WhiteQueen(Reine, PieceBlanche):
    pass


class BlackKing(Roi, PieceNoire):
    pass


class WhiteKing(Roi, PieceBlanche):
    pass
