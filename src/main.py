import pygame
from grid import Grid
from astar import astar
from agent import Agent

pygame.init()

WIDTH = 600
ROWS = 30
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Autonomous Navigation System")

grid = Grid(ROWS, WIDTH)
agent = Agent()

run = True
while run:
    grid.draw(WIN)

    path = astar(grid.grid, grid.start, grid.end)

    if path:
        agent.move(path, grid)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()