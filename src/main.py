from graphics import Window
from cell import Cell
from maze import Maze
def main():
    CELL_SIZE = 20
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    margin = int(.5 * CELL_SIZE)

    num_rows = (WINDOW_HEIGHT - margin) // CELL_SIZE
    num_cols = (WINDOW_WIDTH - margin) // CELL_SIZE
    win = Window(WINDOW_WIDTH, WINDOW_HEIGHT)
    
    maze = Maze(margin, margin, num_rows, num_cols, CELL_SIZE, CELL_SIZE, win)
    result = maze.solve()
    if result:
        print("Solve complete!")
    else:
        print("Failed to solve maze.")
    win.wait_for_close()


if __name__ == '__main__':
    main()