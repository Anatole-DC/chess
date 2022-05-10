from asyncio.format_helpers import _format_callback_source
from shutil import move
_SPOT_WIDTH = 3
from src.pieces.piece import Piece, Option, Forbiden
from src.pieces.movements import *

class Pawn(Piece):
    def __init__(self):
        super().__init__("Pawn", " ♟️ ")

    def get_available_movements(self, spot, chessboard):
        super().get_available_movements(spot, chessboard)
        
        grid = chessboard._grid

        available_movements = []

        try:

            # On vérifie si le pion est sur la ligne de départ pour savoir si il peut bouger de deux ou de 1
            number_of_vertical_movements = 2 if spot._coordinates[0] == 1 else 1

            # Pour chaque mouvements on vérifie si il n'y a pas de jeton
            for i in range(1, number_of_vertical_movements + 1):
                potential_spot = grid[spot._coordinates[0] + i][spot._coordinates[1]]

                if potential_spot.is_empty():
                    available_movements.append(potential_spot)

                # Si oui, on arrête de vérifier.
                else:
                    break

        except Exception as error:
            print(f"Excepetion raised : {error}")


        # Comme c'est un pion, on vérifie également si il n'y a pas de cibles en diagonal.
        for target in self.get_targets(spot, chessboard):
            if not target.is_empty():
                available_movements.append(target)

        return available_movements

    def get_targets(self, spot, chessboard):
        super().get_targets(spot, chessboard)

        grid = chessboard._grid

        targets = []

        try:
            # On récupère les emplacements en diagonal
            potential_targets = [
                grid[spot._coordinates[0] + 1][spot._coordinates[1] - 1],
                grid[spot._coordinates[0] + 1][spot._coordinates[1] + 1]
            ]

            for target in potential_targets:
                # On vérifie si c'est bien un pion adverse
                if not isinstance(target._piece, Piece) or target._piece.color() != self.color():
                    targets.append(target)
        except Exception as error:
            print(f"Excepetion raised : {error}")
        return targets


class King(Piece):
    def __init__(self):
        super().__init__("King", " ♚ ")

    def get_available_movements(self, spot, chessboard):
        super().get_available_movements(spot, chessboard)

        grid = chessboard._grid

        available_movements = []
        try:
            # Diagonal directions

            for i in range(1, 2):
                if 7 >= spot._coordinates[0] + i >= 0 and 7 >= spot._coordinates[1] + i >= 0:
                    if not grid[spot._coordinates[0] + i][spot._coordinates[1] + i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] + i][spot._coordinates[1] + i])

            for i in range(1, 2):
                if 7 >= spot._coordinates[0] + i >= 0 and 7 >= spot._coordinates[1] - i >= 0:
                    if not grid[spot._coordinates[0] + i][spot._coordinates[1] - i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] + i][spot._coordinates[1] - i])

            for i in range(1, 2):
                if 7 >= spot._coordinates[0] - i >= 0 and 7 >= spot._coordinates[1] + i >= 0:
                    if not grid[spot._coordinates[0] - i][spot._coordinates[1] + i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] - i][spot._coordinates[1] + i])

            for i in range(1, 2):
                if 7 >= spot._coordinates[0] - i >= 0 and 7 >= spot._coordinates[1] - i >= 0:
                    if not grid[spot._coordinates[0] - i][spot._coordinates[1] - i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] - i][spot._coordinates[1] - i])

            # Straight directions
            for i in range(1, 2):
                if 7 >= spot._coordinates[0] >= 0 and 7 >= spot._coordinates[1] + i >= 0:
                    if not grid[spot._coordinates[0]][spot._coordinates[1] + i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0]][spot._coordinates[1] + i])

            for i in range(1, 2):
                if 7 >= spot._coordinates[0] >= 0 and 7 >= spot._coordinates[1] - i >= 0:
                    if not grid[spot._coordinates[0]][spot._coordinates[1] - i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0]][spot._coordinates[1] - i])

            for i in range(1, 2):
                if 7 >= spot._coordinates[0] - i >= 0 and 7 >= spot._coordinates[1] >= 0:
                    if not grid[spot._coordinates[0] - i][spot._coordinates[1]].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] - i][spot._coordinates[1]])

            for i in range(1, 2):
                if 7 >= spot._coordinates[0] + i >= 0 and 7 >= spot._coordinates[1] >= 0:
                    if not grid[spot._coordinates[0] + i][spot._coordinates[1]].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] + i][spot._coordinates[1]])

        except Exception as error:
            print(f"Exception was raised : {error}")

        # On doit aller chercher tous les pions de la couleur opposée pour trouver quelles sont les cases sur lesquelles le roi ne peut pas se rendre
        forbiden_spots = []
        for line in grid:
            for spt in line:
                if not spt.is_empty():
                    if spt._piece.color() != self.color() and not isinstance(spt._piece, King):
                        print(spt._piece)
                        forbiden_spots = forbiden_spots + chessboard.get_spot_targets(spt)

        # On enlève des déplacements du roi les déplacements interdits
        for spt in forbiden_spots:
            for move in available_movements:
                if spt._coordinates == move._coordinates:
                    available_movements.remove(spt)

        return available_movements

    def get_targets(self, spot, grid):
        super().get_available_movements(spot, grid)
        return self.get_available_movements(spot, grid)

class Queen(Piece):
    def __init__(self):
        super().__init__("Queen", " ♛ ", all_directions(8))

    def get_available_movements(self, spot, chessboard):
        super().get_available_movements(spot, chessboard)

        grid = chessboard._grid
        available_movements = []
        try:
            # Diagonal directions

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] + i >= 0 and 7 >= spot._coordinates[1] + i >= 0:
                    if not grid[spot._coordinates[0] + i][spot._coordinates[1] + i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] + i][spot._coordinates[1] + i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] + i >= 0 and 7 >= spot._coordinates[1] - i >= 0:
                    if not grid[spot._coordinates[0] + i][spot._coordinates[1] - i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] + i][spot._coordinates[1] - i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] - i >= 0 and 7 >= spot._coordinates[1] + i >= 0:
                    if not grid[spot._coordinates[0] - i][spot._coordinates[1] + i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] - i][spot._coordinates[1] + i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] - i >= 0 and 7 >= spot._coordinates[1] - i >= 0:
                    if not grid[spot._coordinates[0] - i][spot._coordinates[1] - i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] - i][spot._coordinates[1] - i])

            # Straight directions
            for i in range(1, 8):
                if 7 >= spot._coordinates[0] >= 0 and 7 >= spot._coordinates[1] + i >= 0:
                    if not grid[spot._coordinates[0]][spot._coordinates[1] + i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0]][spot._coordinates[1] + i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] >= 0 and 7 >= spot._coordinates[1] - i >= 0:
                    if not grid[spot._coordinates[0]][spot._coordinates[1] - i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0]][spot._coordinates[1] - i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] - i >= 0 and 7 >= spot._coordinates[1] >= 0:
                    if not grid[spot._coordinates[0] - i][spot._coordinates[1]].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] - i][spot._coordinates[1]])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] + i >= 0 and 7 >= spot._coordinates[1] >= 0:
                    if not grid[spot._coordinates[0] + i][spot._coordinates[1]].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] + i][spot._coordinates[1]])


        except Exception as error:
            print(f"Exception was raised : {error}")

        return available_movements

    def get_targets(self, spot, grid):
        super().get_available_movements(spot, grid)
        return self.get_available_movements(spot, grid)


class Bishop(Piece):
    def __init__(self):
        super().__init__("Bishop", " ♝ ")

    def get_available_movements(self, spot, chessboard):
        super().get_available_movements(spot, chessboard)

        grid = chessboard._grid
        available_movements = []
        try:
            potential_spot = []
            
            for i in range(1, 8):
                if 7 >= spot._coordinates[0] + i >= 0 and 7 >= spot._coordinates[1] + i >= 0:
                    if not grid[spot._coordinates[0] + i][spot._coordinates[1] + i].is_empty():
                        break
                    potential_spot.append(grid[spot._coordinates[0] + i][spot._coordinates[1] + i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] + i >= 0 and 7 >= spot._coordinates[1] - i >= 0:
                    if not grid[spot._coordinates[0] + i][spot._coordinates[1] - i].is_empty():
                        break
                    potential_spot.append(grid[spot._coordinates[0] + i][spot._coordinates[1] - i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] - i >= 0 and 7 >= spot._coordinates[1] + i >= 0:
                    if not grid[spot._coordinates[0] - i][spot._coordinates[1] + i].is_empty():
                        break
                    potential_spot.append(grid[spot._coordinates[0] - i][spot._coordinates[1] + i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] - i >= 0 and 7 >= spot._coordinates[1] - i >= 0:
                    if not grid[spot._coordinates[0] - i][spot._coordinates[1] - i].is_empty():
                        break
                    potential_spot.append(grid[spot._coordinates[0] - i][spot._coordinates[1] - i])

            for test_spot in potential_spot:
                available_movements.append(test_spot)

        except Exception as error:
            print(f"Exception was raised : {error}")

        return available_movements

    def get_targets(self, spot, grid):
        super().get_available_movements(spot, grid)
        return self.get_available_movements(spot, grid)


class Rook(Piece):
    def __init__(self):
        super().__init__("Rook", " ♜ ")

    def get_available_movements(self, spot, chessboard):
        super().get_available_movements(spot, chessboard)

        grid = chessboard._grid
        available_movements = []
        try:

            # Straight directions
            for i in range(1, 8):
                if 7 >= spot._coordinates[0] >= 0 and 7 >= spot._coordinates[1] + i >= 0:
                    if not grid[spot._coordinates[0]][spot._coordinates[1] + i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0]][spot._coordinates[1] + i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] >= 0 and 7 >= spot._coordinates[1] - i >= 0:
                    if not grid[spot._coordinates[0]][spot._coordinates[1] - i].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0]][spot._coordinates[1] - i])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] - i >= 0 and 7 >= spot._coordinates[1] >= 0:
                    if not grid[spot._coordinates[0] - i][spot._coordinates[1]].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] - i][spot._coordinates[1]])

            for i in range(1, 8):
                if 7 >= spot._coordinates[0] + i >= 0 and 7 >= spot._coordinates[1] >= 0:
                    if not grid[spot._coordinates[0] + i][spot._coordinates[1]].is_empty():
                        break
                    available_movements.append(grid[spot._coordinates[0] + i][spot._coordinates[1]])


        except Exception as error:
            print(f"Exception was raised : {error}")

        return available_movements

    def get_targets(self, spot, grid):
        super().get_available_movements(spot, grid)
        return self.get_available_movements(spot, grid)


class Knight(Piece):
    def __init__(self):
        super().__init__("Knight", " ♞ ", [
            (2, -1),
            (2, 1),
            (-2, 1),
            (-2, -1)
        ])

    def get_available_movements(self, spot, chessboard):
        super().get_available_movements(spot, chessboard)

        grid = chessboard._grid
        movements = []
        for mvt in self._mvt:
            try:
                potential_spot = grid[spot._coordinates[0] + mvt[0]][spot._coordinates[1] + mvt[1]]

                if potential_spot.is_empty():
                    movements.append(potential_spot)


            except Exception as error:
                print(f"Exception was raised : {type(error)}")
        return movements

    def get_targets(self, spot, grid):
        super().get_available_movements(spot, grid)
        return self.get_available_movements(spot, grid)
