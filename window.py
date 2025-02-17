from tkinter import Tk, BOTH, Canvas
from line import Line

# draws the window
class Window():
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, width=width, height=height)
        self._canvas.pack()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
    
    # draw a line
    def draw_line(self, line, fill_color):
        line.draw(self._canvas, fill_color)

    # redraw every frame
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    # loops perpetually until close
    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
    
    # called on close
    def close(self):
        self._running = False