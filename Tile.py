TILE_SIZE = 25

class Tile:
    def __init__(self,x,y, canvas):
        self.x = x
        self.y = y
        self.visited = False
        #we initialize the neighbours to none, it will cahnge later in the programm
        self.neighbours = {"leftTile" : None, "rightTile" : None, "topTile" : None, "bottomTile" : None}
        #self.rectangle = canvas.create_rectangle(x,y,x + TILE_SIZE, y + TILE_SIZE, bg="white")
        #wall position to draw them
        self.topLeftCornerX = self.x
        self.topLeftCornerY = self.y
        self.bottomLeftCornerX = self.x 
        self.bottomLeftCornerY = self.y + TILE_SIZE
        self.topRightCornerX = self.x + TILE_SIZE
        self.topRightCornerY = self.y
        self.bottomRightCornerX = self.x + TILE_SIZE
        self.bottomRightCornerY = self.y + TILE_SIZE

        #coordinates of the walls 
        self.draw_walls(canvas)

    def draw_walls(self,canvas):
        self.draw_top_wall(canvas)
        self.draw_left_wall(canvas)   
        self.draw_bottom_wall(canvas)         
        self.draw_right_wall(canvas)

    def draw_left_wall(self, canvas):
        self.leftWall = canvas.create_line(self.topLeftCornerX,self.topLeftCornerY, self.bottomLeftCornerX, self.bottomLeftCornerY, width=2, fill="black")
    
    def draw_right_wall(self, canvas):
        self.rightWall = canvas.create_line(self.bottomRightCornerX, self.bottomRightCornerY, self.topRightCornerX, self.topRightCornerY, width=2, fill="black")

    def draw_top_wall(self, canvas):
        self.topWall = canvas.create_line(self.topLeftCornerX,self.topLeftCornerY, self.topRightCornerX, self.topRightCornerY, width=2, fill="black")

    def draw_bottom_wall(self,canvas):
        self.bottomWall = canvas.create_line(self.bottomLeftCornerX, self.bottomLeftCornerY, self.bottomRightCornerX, self.bottomRightCornerY, width=2, fill="black")

    def removeWall(self,canvas,nextTile): 
        if nextTile == self.neighbours["leftTile"]:
            canvas.delete(self.leftWall)
            canvas.delete(nextTile.rightWall) #if the next tile is the one to our left then we destroy our left wall and the next tile right wall
        elif nextTile == self.neighbours["rightTile"]:
            canvas.delete(self.rightWall)
            canvas.delete(nextTile.leftWall) 
        elif nextTile == self.neighbours["topTile"]:
            canvas.delete(self.topWall)
            canvas.delete(nextTile.bottomWall) 
        elif nextTile == self.neighbours["bottomTile"]:
            canvas.delete(self.bottomWall)
            canvas.delete(nextTile.topWall) 

    def listOfUnvisitedNeigbhours(self) -> bool:
        """
        Allows use to loop while we still have unvisited neighbours
        """
        listOfUnvisitedNeighbours = []
        for tile in self.neighbours.values():
            if tile != None and tile.visited == False:
                listOfUnvisitedNeighbours.append(tile)
        return listOfUnvisitedNeighbours
    
    def addNeigbhour(self, tile):
        if tile != None:
            if tile.x < self.x:
                self.neighbours["leftTile"] = tile
            elif tile.y < self.y:
                self.neighbours["topTile"] = tile
            elif tile.x > self.x:
                self.neighbours["rightTile"] = tile
            elif tile.y > self.y:
                self.neighbours["bottomTile"] = tile
