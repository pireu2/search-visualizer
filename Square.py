import pygame
from constants import SQUARE_SIZE, BACKGROUND_COLOR

class Square:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def __eq__(self, other):
        return self.row == other.row and self.col == other.col
    
    def __hash__(self):
        return hash((self.row, self.col))

    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.col * SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_pos(self):
        return self.row, self.col
    
    def erase(self, window):
        self.color = BACKGROUND_COLOR
        self.draw(window)
