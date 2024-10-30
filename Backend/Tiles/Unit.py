from abc import ABC

from Backend.Tiles.EmptyTile import EmptyTile
from Backend.Tiles.Position import Position
from Backend.Tiles.Tile import Tile
from Backend.Tiles.Wall import Wall
from Backend.VisitorInterfaces.Visitor import Visitor
import random


class Unit(Tile, Visitor, ABC):

    def __init__(self, tile: str, x: int, y: int, name: str, health_pool: int, attack_points: int, defense_points: int):
        Tile.__init__(self, tile=tile, x=x, y=y)

        self.name: str = name
        self.health_pool: int = health_pool
        self.health_amount: int = health_pool
        self.attack_points: int = attack_points
        self.defense_points: int = defense_points

    def interact(self, tile: Tile) -> None:
        tile.accept(self)

    def visit_wall(self, wall: Wall) -> None:
        return

    def visit_empty_tile(self, empty: EmptyTile) -> None:
        temp: Position = empty.position

        empty.position = self.position
        self.position = temp

    def get_name(self) -> str:
        return self.name

    def description(self) -> str:
        return (f"--- {self.name} ---\n" + f"{self.health_amount} / {self.health_amount} 🩸\n" +
                f"{self.attack_points} ⚔️    {self.defense_points} 🛡️\n")
      
    def is_dead(self) -> bool:
        return self.health_amount <= 0

    def attack(self, opponent: 'Unit') -> None:
        dmg: int = random.randint(0, self.attack_points)
        opponent.defend(dmg)

    def defend(self, dmg: int) -> None:
        defence: int = random.randint(0, self.defense_points)

        if dmg > defence:
            self.health_amount -= dmg - defence

