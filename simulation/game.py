# game.py

import pygame
from simulation.world import World
from simulation.config import SCREEN_WIDTH, SCREEN_HEIGHT, MIN_ZOOM, MAX_ZOOM
from simulation.utils.rendering import draw_world, draw_minimap

class Game:
    def __init__(self):
        self.world = World()
        self.zoom_level = 3
        self.pan_offset = [0, 0]
    
    def handle_zoom(self, zoom_in):
        if zoom_in and self.zoom_level < MAX_ZOOM:
            self.zoom_level += 1
        elif not zoom_in and self.zoom_level > MIN_ZOOM:
            self.zoom_level -= 1

    def handle_pan(self, direction):
        pan_speed = 10
        if direction == 'up':
            self.pan_offset[1] -= pan_speed
        elif direction == 'down':
            self.pan_offset[1] += pan_speed
        elif direction == 'left':
            self.pan_offset[0] -= pan_speed
        elif direction == 'right':
            self.pan_offset[0] += pan_speed
    
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Zoomable World with Minimap')

        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEWHEEL:
                    self.handle_zoom(event.y > 0)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.handle_pan('up')
                    elif event.key == pygame.K_DOWN:
                        self.handle_pan('down')
                    elif event.key == pygame.K_LEFT:
                        self.handle_pan('left')
                    elif event.key == pygame.K_RIGHT:
                        self.handle_pan('right')

            draw_world(screen, self.world.get_bits(), self.zoom_level, self.pan_offset)
            draw_minimap(screen, self.world.get_bits(), self.pan_offset, self.zoom_level)

            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
