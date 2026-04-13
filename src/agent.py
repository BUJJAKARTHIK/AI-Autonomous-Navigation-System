import pygame
import time

BLUE = (0,0,255)

class Agent:
    def move(self, path, grid):
        gap = grid.width // grid.rows

        for pos in path:
            pygame.draw.rect(pygame.display.get_surface(), BLUE,
                             (pos[1]*gap, pos[0]*gap, gap, gap))
            pygame.display.update()
            time.sleep(0.1)