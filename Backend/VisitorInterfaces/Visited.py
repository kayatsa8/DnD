from abc import ABC, abstractmethod

from Backend.VisitorInterfaces.Visitor import Visitor


class Visited(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


