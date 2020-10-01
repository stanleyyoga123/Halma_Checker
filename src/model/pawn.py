from .color import Color

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

    def __eq__(self, pawn):
        return self.position.location == pawn.position.location

    def copy(self, position):
        temp_pawn = Pawn(self.id, position, self.color)
        temp_pawn.has_red = self.has_red
        temp_pawn.has_green = self.has_red
        temp_pawn.has_neutral = self.has_neutral

        return temp_pawn