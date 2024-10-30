from abc import ABC, abstractmethod
from typing import List

from Backend.Board import Board
from Backend.Tiles.Unit import Unit


class HeroicUnit(ABC):

    @abstractmethod
    def cast_ability(self, units: List[Unit]) -> None:
        pass

