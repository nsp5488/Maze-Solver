from graphics import Window
from cell import Cell
from maze import Maze
def main():
    win = Window(800, 600)

    maze = Maze(5, 5, 10, 10, 15, 15, win)
    print(maze.solve())
    
    win.wait_for_close()


if __name__ == '__main__':
    main()