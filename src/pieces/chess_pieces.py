from shutil import move
from src.pieces.piece import Piece, Option
from src.pieces.movements import *

class Pawn(Piece):
    def __init__(self):
        super().__init__("Pawn", " ♟️ ")

    def get_available_movements(self, spot, grid):
        available_movements = []
        for i in range(1, 3):
            try:
                potential_spot = grid[spot._coordinates[0] + i][spot._coordinates[1]]

                if potential_spot.is_empty():
                    potential_spot._piece = Option()
                    available_movements.append(potential_spot)
                else:
                    break

                potential_targets = [
                    grid[spot._coordinates[0] + i][spot._coordinates[1]-1],
                    grid[spot._coordinates[0] + i][spot._coordinates[1]+1]
                ]

                for target in potential_targets:
                    if not target.is_empty() and target._piece.color() != self.color():
                        available_movements.append(target)
            except Exception as error:
                print(f"Excepetion raised : {type(error)}")

        return available_movements


class King(Piece):
    def __init__(self):
        super().__init__("King", " ♚ ")

    def get_available_movements(self, spot, grid):
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

        for movement in available_movements:
            movement._piece = Option()

        return available_movements


class Queen(Piece):
    def __init__(self):
        super().__init__("Queen", " ♛ ", all_directions(8))

    def get_available_movements(self, spot, grid):
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

        for movement in available_movements:
            movement._piece = Option()

        return available_movements


class Bishop(Piece):
    def __init__(self):
        super().__init__("Bishop", " ♝ ")

    def get_available_movements(self, spot, grid):
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
                test_spot._piece = Option()
                available_movements.append(test_spot)

        except Exception as error:
            print(f"Exception was raised : {error}")

        return available_movements


class Rook(Piece):
    def __init__(self):
        super().__init__("Rook", " ♜ ")

    def get_available_movements(self, spot, grid):
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

        for movement in available_movements:
            movement._piece = Option()

        return available_movements


class Knight(Piece):
    def __init__(self):
        super().__init__("Knight", " ♞ ", [
            (2, -1),
            (2, 1),
            (-2, 1),
            (-2, -1)
        ])

    def get_available_movements(self, spot, grid):
        movements = []
        for mvt in self._mvt:
            try:
                potential_spot = grid[spot._coordinates[0] + mvt[0]][spot._coordinates[1] + mvt[1]]

                if potential_spot.is_empty():
                    potential_spot._piece = Option()
                    movements.append(potential_spot)
            except Exception as error:
                print(f"Exception was raised : {type(error)}")
        return movements
