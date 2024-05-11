from graphics import Point
from graphics import Line

class Cell:
    def __init__(self, window):
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.__window = window

        self.has_left = True
        self.has_top = True
        self.has_right = True
        self.has_bottom = True
        self.visited = False

        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.__window is not None:
            
            color = "#d9d9d9"
            if self.has_top:
                color = 'black'
            self.__window.draw(Line(Point(x1, y1), Point(x2, y1)), color)

            color = "#d9d9d9"
            if self.has_right:
                color = 'black'
            self.__window.draw(Line(Point(x2, y1), Point(x2, y2)), color)

            color = "#d9d9d9"
            if self.has_bottom:
                color = 'black'
            self.__window.draw(Line(Point(x1, y2), Point(x2, y2)), color)
            
            color = "#d9d9d9"
            if self.has_left:
                color = 'black'
            self.__window.draw(Line(Point(x1, y1), Point(x1, y2)), color)

    def draw_move(self, to_cell, undo=False):
        this_center_x = (self._x1 + self._x2) // 2
        this_center_y = (self._y1 + self._y2) // 2
        other_center_x = (to_cell._x1 + to_cell._x2) // 2
        other_center_y = (to_cell._y1 + to_cell._y2) // 2
        
        line = Line(Point(this_center_x, this_center_y), Point(other_center_x, other_center_y))
        if self.__window is not None:
            if undo:
                self.__window.draw(line, "red")
            else:
                self.__window.draw(line, "gray")

    def __repr__(self):
        return f"Cell(({self._x1},{self._y1}), ({self._x2}, {self._y2}): {self.visited})"