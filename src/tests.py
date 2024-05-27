import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        rows = 10
        cols = 12
        maze = Maze(0, 0, rows, cols, 10, 10)

        self.assertEqual(
            len(maze._cells[0]),
            rows,
        )
        self.assertEqual(
            len(maze._cells),
            cols,
        )

    def test_maze_can_break_entrance_exit(self):
        rows = 10
        cols = 12
        maze = Maze(0, 0, rows, cols, 10, 10)
        maze._break_entrance_and_exit()

        self.assertEqual(maze._cells[0][0].has_top_wall, False)
        self.assertEqual(maze._cells[-1][-1].has_bottom_wall, False)


if __name__ == "__main__":
    unittest.main()
