import pygame
from Square import Square
from DrawModes import DrawModes
from constants import *

class Grid:
    def __init__(self, window):
        self.squares = [[Square(row,col,BACKGROUND_COLOR) for col in range(GRID_SIZE)] for row in range(GRID_SIZE)]
        self.window = window
        self.wall_color = DARKER_GRAY
        self.starting_color = YELLOW
        self.end_color = PINK
        self.path_color = RED

        self.starting_point = None
        self.ending_point = None

        self._mode = DrawModes.WALL
    
    def draw_grid(self):
        for i in range(0, WIDTH, SQUARE_SIZE):
            pygame.draw.line(self.window, LITE_GRAY, (i, 0), (i, HEIGHT))
        for i in range(0, HEIGHT, SQUARE_SIZE):
            pygame.draw.line(self.window, LITE_GRAY, (0, i), (WIDTH, i))

    def draw_squares(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.squares[row][col] is not None:
                    self.squares[row][col].draw(self.window)

    def reset_colors(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.squares[row][col].color != self.wall_color and self.squares[row][col].color != self.starting_color and self.squares[row][col].color != self.end_color: 
                    self.squares[row][col].color = BACKGROUND_COLOR

    def can_search(self):
        return self.starting_point is not None and self.ending_point is not None and self.starting_point != self.ending_point and self.starting_point.color != self.wall_color and self.ending_point.color != self.wall_color

    def get_color(self):
        if self._mode == DrawModes.WALL:
            return self.wall_color
        elif self._mode == DrawModes.START:
            return self.starting_color
        elif self._mode == DrawModes.END:
            return self.end_color

    def set_mode(self, mode):
        self._mode = mode

    def handle_click(self, pos):
        x, y = pos
        if x >= WIDTH or y >= HEIGHT:
            return
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE

        if self._mode == DrawModes.START:
            if self.starting_point is not None:
                self.starting_point.color = BACKGROUND_COLOR
                self.starting_point.draw(self.window)
            self.starting_point = self.squares[row][col]
            self.starting_point.color = self.get_color()
        elif self._mode == DrawModes.END:
            if self.ending_point is not None:
                self.ending_point.color = BACKGROUND_COLOR
                self.ending_point.draw(self.window)
            self.ending_point = self.squares[row][col]
            self.ending_point.color = self.get_color()
        else:
            self.squares[row][col].color = self.get_color()
        

