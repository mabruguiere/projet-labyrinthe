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
        for tile in self.tileList:
            self.addNeihgboursToTile(tile)
        #we add to every tile their neighbour
        
    
    def recursive_dfs(self, canvas):
        for tile in self.tileList:
            tile.draw_walls(canvas)
        
        #We first choose a random tile from the Maze to start from
        startTileX = randrange(0 * TILE_SIZE , 25 * TILE_SIZE, TILE_SIZE)
        startTileY = randrange(0 * TILE_SIZE , 25 * TILE_SIZE, TILE_SIZE) #important to add TILE_SIZE as the step to get valid coordinates
        currentTile = self.getTileFromCoor(startTileX,startTileY)

        self.drawMaze(currentTile, canvas, DEFAULT_CONSTRUCTION_SPEED)
    
    def recursive_division(self, canvas, startX : int, endX : int, startY : int, endY : int):
        height = endY - startY
        width = endX - startX 
        if height > width:
            vertical = False
        elif width > height:
            vertical = True
        else:
            vertical = random.choice([True,False])

        if width < TILE_SIZE * 2 or height < TILE_SIZE * 2: #base case, if the section become to small wqe stop
            return

        #Can we continue ? 
        if vertical:
            #choosing which tile won't have a wall
            noWallCoor  = random.randrange(0,height, 25) #pose problème car pas a jout selon recursion
            # choosing where to trace the walls
            x = random.randrange(startX,endX, 25)
            for tile in self.tileList:
                if tile.x == x and tile.y != noWallCoor and startY < tile.y and tile.y < endY:
                    tile.draw_left_wall(canvas)
                    if tile.neighbours["leftTile"] != None:
                        tile.neighbours["leftTile"].draw_right_wall(canvas )
            canvas.update()
            canvas.after(10)
            self.recursive_division(canvas, startX , x , startY, endY)
            self.recursive_division(canvas, x , endX , startY, endY)
        else: # horizontal case
            #choosing which tile won't have a wall
            noWallCoor  = random.randrange(0,width, 25)
            # choosing where to trace the walls
            y = random.randrange(startY,endY, 25)
            for tile in self.tileList:
                if tile.y == y and tile.x != noWallCoor and startX < tile.x and tile.x < endX:
                    tile.draw_bottom_wall(canvas)
                    if tile.neighbours["bottomTile"] != None:
                        tile.neighbours["bottomTile"].draw_top_wall(canvas )
            canvas.update()
            canvas.after(10)
            self.recursive_division(canvas, startX , endX , startY, y)
            self.recursive_division(canvas, startX , endX , y, endY)

        

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