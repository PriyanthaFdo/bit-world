import pygame
from simulation.config import *


def draw_world(screen, bits):
    screen.fill(WHITE)  # Clear the screen
    pygame.draw.rect(screen, BLACK, (0, 0, WORLD_WIDTH + 4, WORLD_HEIGHT + 4), 2)

    for bit in bits:
        x, y = bit.get_position()
        pygame.draw.rect(
            screen, BIT_COLOR, (x + 2, y + 2, BIT_SIZE, BIT_SIZE)
        )  # offset for border


def draw_minimap(screen, bits):
    """Draw the minimap in the bottom-right corner."""
    minimap_x = WORLD_WIDTH + MINIMAP_MARGIN + 4
    minimap_y =  MINIMAP_MARGIN
    pygame.draw.rect(
        screen, (0, 0, 0), (minimap_x, minimap_y, MINIMAP_WIDTH, MINIMAP_HEIGHT)
    )

    scale_x = MINIMAP_WIDTH / WORLD_WIDTH
    scale_y = MINIMAP_HEIGHT / WORLD_HEIGHT

    # Draw bits on the minimap
    for bit in bits:
        bit_x, bit_y = bit.get_position()
        mini_x = minimap_x + int(bit_x * scale_x)
        mini_y = minimap_y + int(bit_y * scale_y)
        pygame.draw.rect(screen, BIT_COLOR, (mini_x, mini_y, 2, 2))
