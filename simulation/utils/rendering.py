# utils/rendering.py

import pygame
from simulation.config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BIT_COLOR, VIEWPORT_COLOR, MINIMAP_MARGIN,
    MINIMAP_WIDTH, MINIMAP_HEIGHT, WORLD_SIZE
)

def draw_world(screen, bits, zoom_level, pan_offset):
    """Draw the world with the current zoom and pan."""
    scale = 9 - zoom_level + 1  # Max zoom level results in max bit size
    bit_size = scale * 3  # Size of a single bit
    
    screen.fill(WHITE)  # Clear the screen

    for bit in bits:
        x, y = bit.get_position()
        x = (x - pan_offset[0]) * bit_size
        y = (y - pan_offset[1]) * bit_size

        if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
            pygame.draw.rect(screen, BIT_COLOR, (x, y, bit_size, bit_size))

# utils/rendering.py

def draw_minimap(screen, bits, pan_offset, zoom_level):
    """Draw the minimap in the bottom-right corner."""
    minimap_x = SCREEN_WIDTH - MINIMAP_WIDTH - MINIMAP_MARGIN
    minimap_y = SCREEN_HEIGHT - MINIMAP_HEIGHT - MINIMAP_MARGIN
    pygame.draw.rect(screen, (0, 0, 0), (minimap_x, minimap_y, MINIMAP_WIDTH, MINIMAP_HEIGHT))

    scale_x = MINIMAP_WIDTH / WORLD_SIZE
    scale_y = MINIMAP_HEIGHT / WORLD_SIZE

    # Draw bits on the minimap
    for bit in bits:
        bit_x, bit_y = bit.get_position()
        mini_x = minimap_x + int(bit_x * scale_x)
        mini_y = minimap_y + int(bit_y * scale_y)
        pygame.draw.rect(screen, BIT_COLOR, (mini_x, mini_y, 2, 2))

    # Draw the FOV rectangle
    scale = 9 - zoom_level + 1
    view_width = SCREEN_WIDTH / (scale * 3)
    view_height = SCREEN_HEIGHT / (scale * 3)

    view_x = minimap_x + int(pan_offset[0] * scale_x)
    view_y = minimap_y + int(pan_offset[1] * scale_y)
    view_rect_width = int(view_width * scale_x)
    view_rect_height = int(view_height * scale_y)

    pygame.draw.rect(screen, VIEWPORT_COLOR, 
                     (view_x, view_y, view_rect_width, view_rect_height), 1)
