import pygame
import random

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

class Grid:
    def __init__(self, rows, width):
        self.rows = rows
        self.width = width
        self.grid = []
        self.start = (0,0)
        self.end = (rows-1, rows-1)
        self.make_grid()

    def make_grid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                # Random obstacles
                if random.random() < 0.2:
                    self.grid[i].append(1)
                else:
                    self.grid[i].append(0)

        self.grid[0][0] = 0
        self.grid[self.rows-1][self.rows-1] = 0

    def draw(self, win):
        gap = self.width // self.rows
        win.fill(WHITE)

        for i in range(self.rows):
            for j in range(self.rows):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(win, BLACK, (j*gap, i*gap, gap, gap))

        pygame.draw.rect(win, GREEN, (0,0,gap,gap))
        pygame.draw.rect(win, RED, ((self.rows-1)*gap,(self.rows-1)*gap,gap,gap))