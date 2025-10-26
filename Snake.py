import tkinter as tk
import random
import Tile

# constant for the display of the tkinter window

ROWS = 25
COLS = 25 
TILE_SIZE = 25 #25 pixels

WINDOW_WIDTH = COLS * TILE_SIZE
WINDOWS_HEIGHT = ROWS * TILE_SIZE

#maze window
windows = tk.Tk()
windows.title("Labyrinthe")
windows.resizable(False,False) 

canvas = tk.Canvas(windows, width=WINDOW_WIDTH, height=WINDOWS_HEIGHT, background="white")
canvas.pack()
windows.update()

#it is better if we center the window
window_width = windows.winfo_width() 
window_height = windows.winfo_height()
screen_width = windows.winfo_screenwidth()
screen_height = windows.winfo_screenheight()

windows_x = int((screen_width/2)-(window_width/2))
windows_y = int((screen_height/2)-(window_height/2))

windows.geometry(f"{window_height}x{window_width}+{windows_x}+{windows_y}") #geometry expect a string not an int

for i in range(ROWS):
    for j in range(COLS):
        test = Tile.Tile(i*TILE_SIZE,j*TILE_SIZE, canvas)

windows.mainloop()