from src.pieces.chess_pieces import *
from src.pieces.piece import BlackPiece, WhitePiece


class BlackPawn(Pawn, BlackPiece):
    pass


class WhitePawn(Pawn, WhitePiece):
    pass


class BlackRook(Rook, BlackPiece):
    pass


class WhiteRook(Rook, WhitePiece):
    pass


class BlackKnight(Knight, BlackPiece):
    pass


class WhiteKnight(Knight, WhitePiece):
    pass


class BlackBishop(Bishop, BlackPiece):
    pass


class WhiteBishop(Bishop, WhitePiece):
    pass


class BlackQueen(Queen, BlackPiece):
    pass


class WhiteQueen(Queen, WhitePiece):
    pass


class BlackKing(King, BlackPiece):
    pass


class WhiteKing(King, WhitePiece):
    pass
