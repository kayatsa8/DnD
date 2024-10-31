from abc import ABC, abstractmethod

from Backend.Tiles.Unit.Player import Player
from Backend.Tiles.Unit.Unit import Unit
from Backend.VisitorInterfaces.Visitor import Visitor


class Enemy(Unit, ABC):

    def __init__(self, tile: str, x: int, y: int, name: str, health_pool: int, attack_points: int, defense_points: int,
                 experience_value: int):
        super().__init__(tile=tile, x=x, y=y, name=name, health_pool=health_pool, attack_points=attack_points,
                         defense_points=defense_points)

        self.experience_value: int = experience_value

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_enemy(self)

    def visit_enemy(self, enemy: 'Enemy') -> None:
        return

    def visit_player(self, player: Player) -> None:
        #TODO initiate fight
        pass
        self.attack(player)

    @abstractmethod
    def on_tick(self):
        pass