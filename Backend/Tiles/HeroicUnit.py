from abc import ABC, abstractmethod

from Backend.Board import Board


class HeroicUnit(ABC):

    @abstractmethod
    def castAbility(self, board: Board) -> None:
        pass

