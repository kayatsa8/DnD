from abc import ABC, abstractmethod
from typing import List

from Backend.Tiles.Unit.Unit import Unit


class HeroicUnit(ABC):

    @abstractmethod
    def cast_ability(self, units: List[Unit]) -> None:
        pass

