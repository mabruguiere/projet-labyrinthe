import Tile

ROWS = 25
COLS = 25
TILE_SIZE = 25

class Maze:
    def __init__(self, canvas):
        for i in range(ROWS):
            for j in range(COLS):
                Tile.Tile(i*TILE_SIZE,j*TILE_SIZE, canvas)