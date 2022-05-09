from typing import List, Tuple

def all_directions(distance: int) -> List[Tuple[int]]:
    return [
        (distance, 0),
        (-distance, 0),
        (distance, distance),
        (-distance, -distance),
        (distance, -distance),
        (-distance, distance),
        (0, distance),
        (0, -distance)
    ]

def up_direction(distance: int) -> List[Tuple[int]]:
    return [
        (distance, 0)
    ]

def diag_direction(distance: int) -> List[Tuple[int]]:
    movements = []
    for i in range(distance):
        movements.append((i, i))
        movements.append((-i, i))
        movements.append((-i, -i))
        movements.append((i, -i))
    return movements