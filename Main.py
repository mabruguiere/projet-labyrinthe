import tkinter as tk
import random
import Maze

# constant for the display of the tkinter window

ROWS = 25
COLS = 25
TILE_SIZE = 25 #25 pixels

WINDOW_WIDTH = COLS * TILE_SIZE
WINDOW_HEIGHT = ROWS * TILE_SIZE

#maze window
windows = tk.Tk()
windows.title("Labyrinthe")
windows.resizable(False,False) 

main_frame = tk.Frame(windows)
main_frame.pack(padx=10, pady=10)

buttons_frame = tk.Frame(main_frame)
buttons_frame.grid(row=0, column=0, padx=10, sticky="n")

canvas = tk.Canvas(main_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, background="white")
canvas.grid(row=0, column=1)

maze = Maze.Maze(canvas)

tk.Button(buttons_frame, text="Prim", command=lambda: maze.prims_algorithm(canvas)).pack(side="top", pady=50)
tk.Button(buttons_frame, text="Division", command=lambda: maze.recursive_division(canvas, 0, ROWS*TILE_SIZE, 0, COLS*TILE_SIZE)).pack(side="top", pady=50)
tk.Button(buttons_frame, text="DFS", command=lambda: maze.recursive_dfs(canvas)).pack(side="top", pady=50)

windows.mainloop()