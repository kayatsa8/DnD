from abc import ABC

from Position import Position


class Tile(ABC):

    def __init__(self, tile: str, x: int, y: int):
        self.tile: str = tile
        self.position: Position = Position(x=x, y=y)

    def Range(self, other: 'Tile') -> float:
        return self.position.Range(other.position)


# @abstractmethod


