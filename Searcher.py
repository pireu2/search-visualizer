from constants import *
from Grid import Grid
import pygame

class Searcher():
    def __init__(self, grid: Grid):
        self.grid = grid
        self.path = []
        self.parent_map = {}


    def get_neighbors(self, square):
        neighbors = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        for direction in directions:
            row = square.row + direction[0]
            col = square.col + direction[1]
            if row >= 0 and row < GRID_SIZE and col >= 0 and col < GRID_SIZE and self.grid.squares[row][col].color != self.grid.wall_color:
                neighbors.append(self.grid.squares[row][col])
        return neighbors
    
    def get_path(self):
        self.path = []
        current = self.grid.ending_point
        while current is not None:
            self.path.insert(0, current)
            current = self.parent_map[current]
        return self.path
    
    def draw_path(self):
        path = self.get_path()
        for square in path:
            if square.color != self.grid.starting_color and square.color != self.grid.end_color:
                square.color = self.grid.path_color
        self.grid.draw_squares()
        pygame.display.update()


    def bfs(self):
        if not self.grid.can_search():
            return
        self.grid.reset_colors()
        queue = [self.grid.starting_point]
        visited = set()
        self.parent_map = {self.grid.starting_point: None}
        while queue:
            current = queue.pop(0)
            if current == self.grid.ending_point:
                self.draw_path()
                return
            visited.add(current)
            if current != self.grid.starting_point and current != self.grid.ending_point:
                current.color = LIGHT_BLUE
            for neighbor in self.get_neighbors(current):
                if neighbor.color == self.grid.wall_color:
                    continue
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    self.parent_map[neighbor] = current
                    if neighbor != self.grid.starting_point and neighbor != self.grid.ending_point:
                        neighbor.color = BLUE
            self.grid.draw_squares()
            self.grid.draw_grid()
            pygame.display.update()

    def dfs(self):
        if not self.grid.can_search():
            return
        self.grid.reset_colors()
        stack = [self.grid.starting_point]
        visited = set()
        self.parent_map = {self.grid.starting_point: None}
        while stack:
            current = stack.pop()
            if current == self.grid.ending_point:
                self.draw_path()
                return
            visited.add(current)
            if current != self.grid.starting_point and current != self.grid.ending_point:
                current.color = LIGHT_BLUE
            for neighbor in self.get_neighbors(current):
                if neighbor.color == self.grid.wall_color:
                    continue
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)
                    self.parent_map[neighbor] = current
                    if neighbor != self.grid.starting_point and neighbor != self.grid.ending_point:
                        neighbor.color = BLUE
            self.grid.draw_squares()
            self.grid.draw_grid()
            pygame.display.update()

    def dijkstra(self):
        if not self.grid.can_search():
            return
        self.grid.reset_colors()
        queue = [self.grid.starting_point]
        visited = set()
        self.parent_map = {self.grid.starting_point: None}
        while queue:
            current = queue.pop(0)
            if current == self.grid.ending_point:
                self.draw_path()
                return
            visited.add(current)
            if current != self.grid.starting_point and current != self.grid.ending_point:
                current.color = LIGHT_BLUE
            for neighbor in self.get_neighbors(current):
                if neighbor.color == self.grid.wall_color:
                    continue
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    self.parent_map[neighbor] = current
                    if neighbor != self.grid.starting_point and neighbor != self.grid.ending_point:
                        neighbor.color = BLUE
            self.grid.draw_squares()
            self.grid.draw_grid()
            pygame.display.update()

    def heuristic(self, square1, square2):
        return abs(square1.row - square2.row) + abs(square1.col - square2.col)

    def a_star(self):
        if not self.grid.can_search():
            return
        self.grid.reset_colors()
        open_set = [self.grid.starting_point]
        closed_set = set()
        self.parent_map = {self.grid.starting_point: None}
        g_score = {self.grid.starting_point: 0}
        f_score = {self.grid.starting_point: self.heuristic(self.grid.starting_point, self.grid.ending_point)}
        while open_set:
            current = open_set[0]
            for square in open_set:
                if f_score[square] < f_score[current]:
                    current = square
            if current == self.grid.ending_point:
                self.draw_path()
                return
            open_set.remove(current)
            closed_set.add(current)
            if current != self.grid.starting_point and current != self.grid.ending_point:
                current.color = LIGHT_BLUE
            for neighbor in self.get_neighbors(current):
                if neighbor.color == self.grid.wall_color:
                    continue
                if neighbor in closed_set:
                    continue
                tentative_g_score = g_score[current] + 1
                if neighbor not in open_set:
                    open_set.append(neighbor)
                elif tentative_g_score >= g_score[neighbor]:
                    continue
                self.parent_map[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + self.heuristic(neighbor, self.grid.ending_point)
                if neighbor != self.grid.starting_point and neighbor != self.grid.ending_point:
                    neighbor.color = BLUE
            self.grid.draw_squares()
            self.grid.draw_grid()
            pygame.display.update()

    def uniform_cost_search(self):
        if not self.grid.can_search():
            return
        self.grid.reset_colors()
        open_set = [self.grid.starting_point]
        closed_set = set()
        self.parent_map = {self.grid.starting_point: None}
        g_score = {self.grid.starting_point: 0}
        while open_set:
            current = open_set[0]
            for square in open_set:
                if g_score[square] < g_score[current]:
                    current = square
            if current == self.grid.ending_point:
                self.draw_path()
                return
            open_set.remove(current)
            closed_set.add(current)
            if current != self.grid.starting_point and current != self.grid.ending_point:
                current.color = LIGHT_BLUE
            for neighbor in self.get_neighbors(current):
                if neighbor.color == self.grid.wall_color:
                    continue
                if neighbor in closed_set:
                    continue
                tentative_g_score = g_score[current] + 1
                if neighbor not in open_set:
                    open_set.append(neighbor)
                elif tentative_g_score >= g_score[neighbor]:
                    continue
                self.parent_map[neighbor] = current
                g_score[neighbor] = tentative_g_score
                if neighbor != self.grid.starting_point and neighbor != self.grid.ending_point:
                    neighbor.color = BLUE
            self.grid.draw_squares()
            self.grid.draw_grid()
            pygame.display.update()
