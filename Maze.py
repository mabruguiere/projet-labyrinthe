import Tile
import random 
from random import randrange
from time import sleep

ROWS = 25
COLS = 25
TILE_SIZE = 25
DEFAULT_CONSTRUCTION_SPEED = 20 #increase for a slower speed

class Maze:
    def __init__(self, canvas):
        self.tileList = []

        self.drawTile(canvas)
        #we add to every tile their neighbour
        for tile in self.tileList:
            self.addNeihgboursToTile(tile)
        
        #We first choose a random tile from the Maze to start from
        startTileX = randrange(0 * TILE_SIZE , 25 * TILE_SIZE, TILE_SIZE)
        startTileY = randrange(0 * TILE_SIZE , 25 * TILE_SIZE, TILE_SIZE) #important to add TILE_SIZE as the step to get valid coordinates
        currentTile = self.getTileFromCoor(startTileX,startTileY)

        self.drawMaze(currentTile, canvas, DEFAULT_CONSTRUCTION_SPEED)

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
    
    def drawMaze(self, currentTile, canvas, speed : int):
        currentTile.visited = True
        rectangle = canvas.create_rectangle(currentTile.x,currentTile.y, currentTile.x + TILE_SIZE, currentTile.y + TILE_SIZE, fill="green")
        univisitedNeighbours = currentTile.listOfUnvisitedNeigbhours()
        while univisitedNeighbours: #while the list of unvisited neighbours is not empty is equivalent to the current tile still having neighbours to visit
            #we choose a random neighbours among the one unvisited, we only have the ones defined (diferent from null)
            nextTile = random.choice(list(univisitedNeighbours)) 
        
            #we want to see the progression of the construction of the maze and not only the final result
            canvas.update()
            canvas.after(speed) 
            
            #Recursive call
            currentTile.removeWall(canvas, nextTile)
            
            canvas.delete(rectangle)
            canvas.update()
            self.drawMaze(nextTile, canvas, speed)

            #We update the list of unvisited neighbours for the backtracking part so we don't stay in the loop forever
            univisitedNeighbours = currentTile.listOfUnvisitedNeigbhours() 

        canvas.delete(rectangle) #this part is mandatory otherwise we would have a green square forever whenever we hit the base case in our recursion
        canvas.update()