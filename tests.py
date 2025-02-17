import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        self.assertEqual(m1._cells[3][7].visited, False)
        m2 = Maze(0, 0, 0, 0, 0, 0)
        self.assertEqual([], m2._cells)
    
    def test_maze_break_entrance_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[11][9].has_bottom_wall, False)
    
if __name__ == "__main__":
    unittest.main()