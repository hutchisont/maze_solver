from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win

        self._cells = []

        if seed is not None:
            random.seed(seed)

        self._create_cells()

    def _create_cells(self):
        self._cells = [
            [Cell(self.win) for _ in range(self.num_rows)]
            for _ in range(self.num_cols)
        ]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return

        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + i * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        # should this really happen every time we update a cell?
        # might be more effecient to just draw them all and then animate them all?
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        # this feels stupid performance wise to me but its what the project
        # says to do. I guess its basically acting as a framerate cap so it
        # doesn't just murder the devices processor and potentially do its thing
        # so quick we can't really see it?
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        last_cell_i = self.num_cols - 1
        last_cell_j = self.num_rows - 1

        self._cells[0][0].has_top_wall = False
        self._cells[last_cell_i][last_cell_j].has_bottom_wall = False

        self._draw_cell(0, 0)
        self._draw_cell(last_cell_i, last_cell_j)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []

            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            random_direction = random.randrange(len(to_visit))
            next = to_visit[random_direction]

            if next[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next[0], next[1])

    def _reset_cells_visited(self):
        for row_cells in self._cells:
            for cell in row_cells:
                cell.visited = False
