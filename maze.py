import time
import random
from cell import Cell

# holds the cells of the maze in a list of lists
class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        random.seed(seed) # for debugging, if None it's just random
        self._cells = []
        self._create_cells()
    
    # populates the array of cells
    def _create_cells(self):
        for i in range(0, self.num_cols):
            self._cells.append([])
            for j in range(0, self.num_rows):
                self._cells[i].append(Cell(self.x1+i*self.cell_size_x, self.x1+(i+1)*self.cell_size_x, self.y1+j*self.cell_size_y, self.y1+(j+1)*self.cell_size_y, self._win))
                self._draw_cell(i, j)
        if len(self._cells) > 0:
            self._break_entrance_and_exit()
            self._break_walls_r(0,0)
            self._reset_cells_visited()
    
    # draws a cell
    def _draw_cell(self, i, j):
        self._cells[i][j].draw("green")
        self._animate()

    # puts a brief pause between frames so it can animate
    def _animate(self):
        if self._win is not None:
            self._win.redraw()
            time.sleep(0.05)
    
    # removes an outer wall of the upper left and lower right corner
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)
    
    # using depth first traversal, breaks walls to form the maze in the first place
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            # left
            if i > 0 and self._cells[i-1][j].visited == False:
                to_visit.append((i-1,j))
            # right
            if i < self.num_cols-1 and self._cells[i+1][j].visited == False:
                to_visit.append((i+1,j))
            # up
            if j > 0 and self._cells[i][j-1].visited == False:
                to_visit.append((i,j-1))
            # down
            if j < self.num_rows-1 and self._cells[i][j+1].visited == False:
                to_visit.append((i,j+1))
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            next_dir = random.randrange(len(to_visit))
            # left
            if i > to_visit[next_dir][0]:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # right
            if i < to_visit[next_dir][0]:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # up
            if j > to_visit[next_dir][1]:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            # down
            if j < to_visit[next_dir][1]:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            self._draw_cell(i,j)
            self._break_walls_r(to_visit[next_dir][0], to_visit[next_dir][1])
    
    # resets whether a cell has been visited or not
    def _reset_cells_visited(self):
        for i in range(0, self.num_cols):
            for j in range(0, self.num_rows):
                self._cells[i][j].visited = False
    
    # returns true if a solution to the maze was found, false otherwise
    def solve(self):
        return self._solve_r(0,0)
    
    # using depth first traversal, searches for a solution to the maze
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        # left
        if i > 0 and self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        # right
        if i < self.num_cols-1 and self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        # up
        if j > 0 and self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        # down
        if j < self.num_rows-1 and self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        return False