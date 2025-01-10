# bit.py

class Bit:
    """Represents a single unit in the world."""
    def __init__(self, position):
        self.position = position  # Position is a tuple (x, y)
    
    def get_position(self):
        return self.position
