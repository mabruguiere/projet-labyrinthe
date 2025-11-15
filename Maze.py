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

        #collection containing all the tile of the maze
        self.tileList = []
        self.addTileToTheMaze(canvas)

        #we add to every tile their neighbours
        for tile in self.tileList:
            self.addNeihgboursToTile(tile)
        
    
    def recursive_dfs(self, canvas):
        """
        Initialize the dfs algorithm by picking the starting cell/tile and starting the algorithm

        Args:
            canvas (tkinter canvas): the canva we will be using to draw the maze
        """
        self.drawEveryTile(canvas)
        
        #We first choose a random tile from the Maze to start from
        startTileX = randrange(0 * TILE_SIZE , 25 * TILE_SIZE, TILE_SIZE)
        startTileY = randrange(0 * TILE_SIZE , 25 * TILE_SIZE, TILE_SIZE) #important to add TILE_SIZE as the step to get valid coordinates
        
        currentTile = self.getTileFromCoor(startTileX,startTileY)

        self.drawMazeWithDFS(currentTile, canvas, DEFAULT_CONSTRUCTION_SPEED)

    def drawMazeWithDFS(self, currentTile, canvas, speed : int):
        """The actual algorithm that implements dfs

        Args:
            currentTile (Tile): The tile where we are right now, the one used to choose one neighbour from
            canvas (tkinter canvas): the canvas used to draw on
            speed (int): the speed at which we will draw our maze, the lower it is the fastest is the drawing
        """
        currentTile.visited = True
        
        #This is the current tile
        currentTile = canvas.create_rectangle(currentTile.x,currentTile.y, currentTile.x + TILE_SIZE, currentTile.y + TILE_SIZE, fill="green")
        
        univisitedNeighbours = currentTile.listOfUnvisitedNeigbhours()
        while univisitedNeighbours: #while the list of unvisited neighbours is not empty is equivalent to the current tile still having neighbours to visit
            #we choose a random neighbours among the one unvisited, we only have the ones defined (diferent from null)
            nextTile = random.choice(list(univisitedNeighbours)) 
        
            #we want to see the progression of the construction of the maze and not only the final result
            canvas.update()
            canvas.after(speed) 
            
            #Recursive call
            currentTile.removeWall(canvas, nextTile)
            
            canvas.delete(currentTile)
            canvas.update()
            self.drawMazeWithDFS(nextTile, canvas, speed)

            #We update the list of unvisited neighbours for the backtracking part so we don't stay in the loop forever
            univisitedNeighbours = currentTile.listOfUnvisitedNeigbhours() 

        canvas.delete(currentTile) #this part is mandatory otherwise we would have a green square forever whenever we hit the base case in our recursion
        canvas.update()
    
    def prims_algorithm(self,canvas):
        """ Initialize the prim algorithm by picking the starting cell/tile and starting the algorithm

        Args:
            canvas (_type_): _description_
        """
        #We pick a random cell
        self.drawEveryTile(canvas)
        
         #We first choose a random tile from the Maze to start from
        startTileX = randrange(0 * TILE_SIZE , 25 * TILE_SIZE, TILE_SIZE)
        startTileY = randrange(0 * TILE_SIZE , 25 * TILE_SIZE, TILE_SIZE) #important to add TILE_SIZE as the step to get valid coordinates
        currentTile = self.getTileFromCoor(startTileX,startTileY)
        self.drawMazeWithPrim(currentTile, canvas)


    def drawMazeWithPrim(self,currentTile : Tile, canvas):
        """The actual algorithm that implements prim

        Args:
            currentTile (Tile): The tile where we are right now, the one used to choose one neighbour from
            canvas (_type_): canvas used to draw on
        """
        tileSet = set()
        currentTile.visited = True

        for neighbour in  currentTile.listOfUnvisitedNeigbhours():
            tileSet.add((currentTile ,neighbour))

        while tileSet: 
            randomTile,randomNeighbourTile = random.choice(list(tileSet))
            tileSet.remove((randomTile, randomNeighbourTile))

            if not randomNeighbourTile.visited:
                randomTile.removeWall(canvas, randomNeighbourTile)
                randomNeighbourTile.visited = True
                for neighbour in randomNeighbourTile.listOfUnvisitedNeigbhours():
                    tileSet.add((randomNeighbourTile, neighbour))
            canvas.update()
            canvas.after(10)



    def recursive_division(self, canvas, startX : int, endX : int, startY : int, endY : int):
        """Implementation of the recursive division algorithm

        Args:
            canvas (_type_): the canvas used to draw on

            The parameters bellow are used because this algoritmh slices the canvas in two part
            so the parameters are used to tell us which part we are working with

            startX (int): The starting abscisse of the area we are working with
            endX (int): The ending abscisse of the area we are working with
            startY (int): The starting Y of the area we are working with
            endY (int): The ending Y of the area we are working with
        """
        height = endY - startY
        width = endX - startX 
        if height > width:
            vertical = False
        elif width > height:
            vertical = True
        else:
            vertical = random.choice([True,False])

        if width < TILE_SIZE * 2 or height < TILE_SIZE * 2: #base case, if the section become to small we stop
            return

        #Can we continue ? 
        if vertical:
            #choosing which tile won't have a wall
            noWallCoor  = random.randrange(startY,endY + TILE_SIZE, TILE_SIZE)
            # choosing where to trace the walls
            x = random.randrange(startX,endX + TILE_SIZE, TILE_SIZE)
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
            noWallCoor = random.randrange(startX,endX + TILE_SIZE, TILE_SIZE)
            # choosing where to trace the walls
            y = random.randrange(startY,endY + TILE_SIZE, TILE_SIZE)
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
        """Given a tile, we add to the maze all of it's neighbour

        Args:
            tile (Tile): _description_
        """
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

    def addTileToTheMaze(self, canvas):
        """We add all the tile objects to the maze

        Args:
            canvas (_type_): the canvas we are using to draw on
        """
        for i in range(ROWS):
            for j in range(COLS):
                tile = Tile.Tile(i*TILE_SIZE,j*TILE_SIZE, canvas)
                self.tileList.append(tile)


    def getTileFromCoor(self, x: int, y: int) -> Tile:
        """Return a tile from a x and y postion

        Args:
            x (int): the abscisse of the tile we are looking for
            y (int): the y of the tile we are looking for

        Returns:
            Tile: the tile that match this coordinates
        """
        for tile in self.tileList:
            if tile.x == x and tile.y == y:
                return tile
            
    def drawEveryTile(self, canvas):
        """Draws the wall of every tile in the maze, we can't draw the wall while adding it to the maze in addTileToTheMaze
        because the recursive division starts with no walls.

        Args:
            canvas (_type_): the canvas we are using to draw
        """
        for tile in self.tileList:
            tile.draw_walls(canvas)
    
