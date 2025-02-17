from line import Line, Point

# a cell knows which walls it has and where it exists in the 2D plane
class Cell():
    def __init__(self, x1, x2, y1, y2, win=None):
        self._win = win
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)
        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)
        self._upper_left = Point(min(x1, x2), min(y1, y2))
        self._upper_right = Point(max(x1, x2), min(y1, y2))
        self._lower_left = Point(min(x1, x2), max(y1, y2))
        self._lower_right = Point(max(x1, x2), max(y1, y2))
        self.visited = False
    
    # draw the cell
    def draw(self, fill_color):
        if self._win is None:
            return

        # it's not quite white, it's actually the background color, but it's fine
        white = "#d9d9d9"

        if self.has_left_wall:
            self._win.draw_line(Line(self._upper_left, self._lower_left), fill_color)
        else:
            self._win.draw_line(Line(self._upper_left, self._lower_left), white)
        if self.has_right_wall:
            self._win.draw_line(Line(self._upper_right, self._lower_right), fill_color)
        else:
            self._win.draw_line(Line(self._upper_right, self._lower_right), white)
        if self.has_top_wall:
            self._win.draw_line(Line(self._upper_left, self._upper_right), fill_color)
        else:
            self._win.draw_line(Line(self._upper_left, self._upper_right), white)
        if self.has_bottom_wall:
            self._win.draw_line(Line(self._lower_right, self._lower_left), fill_color)
        else:
            self._win.draw_line(Line(self._lower_right, self._lower_left), white)
    
    # draw a line from this cell to to_cell
    def draw_move(self, to_cell, undo=False):
        fill_color = "red"
        if undo:
            fill_color = "gray"
        own_midpoint = Point((self.x1 + self.x2)/2, (self.y1 + self.y2)/2)
        to_midpoint = Point((to_cell.x1 + to_cell.x2)/2, (to_cell.y1 + to_cell.y2)/2)
        if self._win is not None:
            self._win.draw_line(Line(own_midpoint, to_midpoint), fill_color)