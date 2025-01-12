import numpy as np
from simulation.bit import Bit
from simulation.config import *

class World:
    """Represents the world grid."""
    def __init__(self):
        self.bits = []
        # Initialize some bits in random positions
        for _ in range(INITIAL_BIT_COUNT): 
            x = np.random.randint(0, WORLD_WIDTH)
            y = np.random.randint(0, WORLD_HEIGHT)
            self.bits.append(Bit((x, y)))
    
    def get_bits(self):
        """Returns all the bits in the world."""
        return self.bits
