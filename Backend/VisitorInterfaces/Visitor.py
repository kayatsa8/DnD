from abc import ABC, abstractmethod

from Backend.Tiles.EmptyTile import EmptyTile
from Backend.Tiles.Enemy.Enemy import Enemy
from Backend.Tiles.Enemy.Enemy import Player
from Backend.Tiles.Wall import Wall


class Visitor(ABC):

    @abstractmethod
    def visit_wall(self, wall: Wall) -> None:
        pass

    @abstractmethod
    def visit_empty_tile(self, empty: EmptyTile) -> None:
        pass

    @abstractmethod
    def visit_player(self, player: Player) -> None:
        pass

    @abstractmethod
    def visit_enemy(self, enemy: Enemy) -> None:
        pass



