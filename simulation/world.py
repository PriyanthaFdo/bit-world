# world.py

import numpy as np
from simulation.bit import Bit
from simulation.config import WORLD_SIZE

class World:
    """Represents the world grid."""
    def __init__(self):
        self.bits = []
        # Initialize some bits in random positions
        for _ in range(100):  # Starting with 100 bits for example
            x = np.random.randint(0, WORLD_SIZE)
            y = np.random.randint(0, WORLD_SIZE)
            self.bits.append(Bit((x, y)))
    
    def get_bits(self):
        """Returns all the bits in the world."""
        return self.bits
