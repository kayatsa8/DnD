from abc import ABC
from typing import List

from Backend.Board import Board
from Backend.Tiles.Unit.Enemy.Enemy import Enemy
from Backend.Tiles.Unit.HeroicUnit import HeroicUnit
from Backend.Tiles.Position import Position
from Backend.Tiles.Tile import Tile
from Backend.Tiles.Unit.Unit import Unit


class Player(Unit, ABC, HeroicUnit):

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

    def visit_player(self, player: 'Player') -> None:
        return

    def visit_enemy(self, enemy: Enemy) -> None:
        self.attack(enemy)

        if enemy.is_dead():
            self.experience += enemy.experience_value
            enemy.name = "toRemove"

            tmp: Position = self.position
            self.position = enemy.position
            enemy.position = tmp

            if self.can_level_up():
                self.level_up()

    def on_tick(self, action: int, board: Board, enemies: List[Enemy]) -> None:
        if action == 'q':
            return

        if action == 'e':
            self.cast_ability(enemies)
            return

        tile: Tile = Tile("", -1, -1)

        if action == 'w':
            tile = board.get_tile(self.position.x, self.position.y - 1)
        elif action == 's':
            tile = board.get_tile(self.position.x, self.position.y + 1)
        elif action == 'd':
            tile = board.get_tile(self.position.x + 1, self.position.y)
        elif action == 'a':
            tile = board.get_tile(self.position.x - 1, self.position.y)

        self.interact(tile)

        board.update_position([self, tile])



