TILE_SIZE = 25

class Tile:
    def __init__(self,x,y, canvas):
        self.x = x
        self.y = y
        self.visited = False
        self.neighbours = []

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
        self.topWall = canvas.create_line(self.topLeftCornerX,self.topLeftCornerY, self.topRightCornerX, self.topRightCornerY, width=2, fill="black")
        self.leftWall = canvas.create_line(self.topLeftCornerX,self.topLeftCornerY, self.bottomLeftCornerX, self.bottomLeftCornerY, width=2, fill="black")
        self.bottomWall = canvas.create_line(self.bottomLeftCornerX, self.bottomLeftCornerY, self.bottomRightCornerX, self.bottomRightCornerY, width=2, fill="black")
        self.rightWall = canvas.create_line(self.bottomRightCornerX, self.bottomRightCornerY, self.topRightCornerX, self.topRightCornerY, width=2, fill="black")

    def addNeigbhour(self, tile):
        self.neighbours.append(tile)