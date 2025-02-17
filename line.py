# helper Point class, holds a point in 2D space
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# draws a line between two points
class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    # draws the line on the passed canvas in the passed color
    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)