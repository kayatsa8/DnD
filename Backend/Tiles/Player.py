from abc import ABC, abstractmethod

from Backend.Tiles.Unit import Unit


class Player(Unit, ABC):

    def __init__(self, tile: str, x: int, y: int, name: str, health_pool: int, attack_points: int, defense_points: int):
        super().__init__(tile, x, y, name, health_pool, attack_points, defense_points)

        self.experience: int = 0
        self.level: int = 1

    def can_level_up(self) -> bool:
        return self.experience == self.level * 50

    def level_up(self) -> None:
        if not self.can_level_up():
            raise Exception("cannot level up yet!")

        self.experience -= 50 * self.level
        self.level += 1
        self.health_pool += 10 * self.level
        self.health_amount = self.health_pool
        self.attack_points += 4 * self.level
        self.defense_points += self.level




