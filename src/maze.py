from cell import Cell
from time import sleep
import random
class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self.__win = win
        if seed is not None:
            random.seed(seed)

        self._create_cells()

    def solve(self):
        print("Solving maze")
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        to_visit = []
        if i > 0 and not self._cells[i -1 ][j].visited and not self._cells[i][j].has_left:
            to_visit.append((i - 1, j))
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not self._cells[i][j].has_right:
            to_visit.append((i + 1, j))
        if j > 0 and not self._cells[i][j - 1].visited and not self._cells[i][j].has_top:
            to_visit.append((i, j - 1))
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not self._cells[i][j].has_bottom:
            to_visit.append((i, j + 1))
        
        if len(to_visit) == 0:
            return False

        res = False
        for neighbor in to_visit:
            self._cells[i][j].draw_move(self._cells[neighbor[0]][neighbor[1]])
            res = self._solve_r(neighbor[0], neighbor[1])
            if res:
                return res
            self._cells[i][j].draw_move(self._cells[neighbor[0]][neighbor[1]], True)

        return res

    def _create_cells(self):
        self._cells = []
        print("Generating maze...")
        for i in range(self._num_cols):
            self._cells.append([None]*self._num_rows)
            for j in range(self._num_rows):
                self._cells[i][j] = Cell(self.__win)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cells(i, j)
        
        self._break_entrance_and_exit()
        self._reset_cells_visited()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()



    def _draw_cells(self, i, j):
        x = self._cell_size_x * i + self._x1
        y = self._cell_size_y * j + self._y1
        x2 = x + self._cell_size_x
        y2 = y + self._cell_size_y

        self._cells[i][j].draw(x, y, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        if random.randint(1, 2) == 1:
            self._cells[0][0].has_left = False
        else:
            self._cells[0][0].has_top = False
        self._draw_cells(0, 0)

        if random.randint(1, 2) == 1:
            self._cells[self._num_cols-1][self._num_rows-1].has_right = False
        else:
            self._cells[self._num_cols-1][self._num_rows-1].has_bottom = False

        self._draw_cells(self._num_cols - 1, self._num_rows - 1)
        

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        self._animate()

        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j, 'left'))
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j, 'right'))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j - 1, 'up'))
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1,'down'))


            if len(to_visit) == 0:
                self._draw_cells(i, j)
                return

            chosen = random.sample(to_visit, 1)[0]
            x = chosen[0]
            y = chosen[1]
            if chosen[2] == 'up':
                self._cells[i][j].has_top = False
                self._cells[x][y].has_bottom = False
            if chosen[2] == 'left':
                self._cells[i][j].has_left = False
                self._cells[x][y].has_right = False
            if chosen[2] == 'down':
                self._cells[i][j].has_bottom = False
                self._cells[x][y].has_top = False
            if chosen[2] == 'right':
                self._cells[i][j].has_right = False
                self._cells[x][y].has_left = False
            

            self._break_walls_r(chosen[0], chosen[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False


    def _animate(self):
        if self.__win is not None:
            self.__win.redraw()
            sleep(.005)