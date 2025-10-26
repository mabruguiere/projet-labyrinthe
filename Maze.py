import Tile

ROWS = 25
COLS = 25
TILE_SIZE = 25

class Maze:
    def __init__(self, canvas):
        self.tileList = []
        self.drawTile(canvas)
        #we add to every tile their neighbour
        for tile in self.tileList:
            self.addNeihgboursToTile(tile)

        """for elt in self.getTileFromCoor(0 * TILE_SIZE,0 * TILE_SIZE).neighbours.values():
            print(f"x : {elt.x}, y : {elt.y}")"""
        # canvas.delete(self.getTileFromCoor(0 * TILE_SIZE,0 * TILE_SIZE).topWall) # après test la ligne suivante marche
        """tile = self.getTileFromCoor(0 * TILE_SIZE,0 * TILE_SIZE)
        nextTile = tile.neighbours["rightTile"]
        tile.removeWall(canvas, nextTile)"""
    
    def addNeihgboursToTile(self, tile : Tile):
        topTileX = tile.x
        topTileY = tile.y - TILE_SIZE
        if(topTileY >= 0):
            tile.addNeigbhour(self.getTileFromCoor(topTileX,topTileY)) # we do it here so we don't add a cell that is outside the canvas
        
        leftTileX = tile.x - TILE_SIZE
        leftTileY = tile.y
        if(leftTileX >= 0):
            tile.addNeigbhour(self.getTileFromCoor(leftTileX,leftTileY)) # we do it here so we don't add a cell that is outside the canvas
        
        bottomTileX = tile.x
        bottomTileY = tile.y + TILE_SIZE
        if(bottomTileY <= ROWS * 25):
            tile.addNeigbhour(self.getTileFromCoor(bottomTileX,bottomTileY)) # we do it here so we don't add a cell that is outside the canvas
        
        rightTileX = tile.x + TILE_SIZE
        rightTileY = tile.y
        if(rightTileX <= COLS * 25):
            tile.addNeigbhour(self.getTileFromCoor(rightTileX,rightTileY)) # we do it here so we don't add a cell that is outside the canvas

    def drawTile(self, canvas):
        #Adding the cell to the maze and drawing them (we draw the wall)
        for i in range(ROWS):
            for j in range(COLS):
                self.tileList.append(Tile.Tile(i*TILE_SIZE,j*TILE_SIZE, canvas))

    def getTileFromCoor(self, x: int, y: int) -> Tile:
        for tile in self.tileList:
            if tile.x == x and tile.y == y:
                return tile
    