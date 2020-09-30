from src.model.color import Color

class Pawn():    
    def __init__(self, id, position, color):
        self.id = id
        self.position = position
        self.color = color
        self.has_red = False
        self.has_green = False
        self.has_neutral = False
    
    def __str__(self):
        if self.color == Color.RED:
            return 'R'
        else:
            return 'G'