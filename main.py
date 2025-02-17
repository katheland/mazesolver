from window import Window
from maze import Maze

def main():
    win = Window(800, 600)
    
    maze = Maze(25, 25, 11, 15, 50, 50, win)
    if maze.solve():
        print("Maze path found!")
    else:
        print("No path found through the maze...")

    win.wait_for_close()

main()