import pygame
from simulation.world import World
from simulation.config import *
from simulation.utils.rendering import draw_world, draw_minimap


class Game:
    def __init__(self):
        self.world = World()

    def run(self):
        pygame.init()

        window_width = WORLD_WIDTH + (MINIMAP_MARGIN * 2) + MINIMAP_WIDTH + 4
        window_height = WORLD_HEIGHT + 4
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Bit World")

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            draw_world(screen, self.world.get_bits())
            draw_minimap(screen, self.world.get_bits())

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
