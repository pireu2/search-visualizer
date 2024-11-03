import pygame
import sys

from Grid import Grid
from DrawModes import DrawModes
from Searcher import Searcher
from constants import *




if __name__ == "__main__":
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Search Algorithm Visualizer")
    drawing = False

    grid = Grid(window)
    searcher = Searcher(grid)

    while True:
        window.fill(BACKGROUND_COLOR)
        grid.draw_squares()
        grid.draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                pos = pygame.mouse.get_pos()
                grid.handle_click(pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.MOUSEMOTION and drawing:
                pos = pygame.mouse.get_pos()
                grid.handle_click(pos)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    grid.set_mode(DrawModes.WALL)
                elif event.key == pygame.K_s:
                    grid.set_mode(DrawModes.START)
                elif event.key == pygame.K_e:
                    grid.set_mode(DrawModes.END)
                elif event.key == pygame.K_r:
                    grid = Grid(window)
                    searcher = Searcher(grid)
                if grid.can_search():
                    if event.key == pygame.K_1:
                        searcher.bfs()
                    elif event.key == pygame.K_2:
                        searcher.dfs()
                    elif event.key == pygame.K_3:
                        searcher.dijkstra()
                    elif event.key == pygame.K_4:
                        searcher.a_star()
                    elif event.key == pygame.K_5:
                        searcher.uniform_cost_search()
        pygame.display.update()




