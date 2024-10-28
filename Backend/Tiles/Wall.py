from Backend.Tiles.Tile import Tile
from Backend.VisitorInterfaces.Visitor import Visitor


class Wall(Tile):

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_wall(self)

