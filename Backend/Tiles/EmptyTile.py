from Backend.Tiles.Tile import Tile
from Backend.VisitorInterfaces.Visitor import Visitor


class EmptyTile(Tile):

    def __init__(self, tile: str, x: int, y: int):
        super().__init__(tile='.', x=x, y=y)

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_empty_tile(self)