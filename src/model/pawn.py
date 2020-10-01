from .color import Color

class Pawn():    
    def __init__(self, id, position, color):
        self.id = id
        self.position = position
        self.color = color

        if color == Color.RED:
            self.has_red = True
            self.has_green = False
        else:
            self.has_green = True
            self.has_red = False

        self.has_neutral = False
    
    def __str__(self):
        if self.color == Color.RED:
            return 'R'
        else:
            return 'G'

    def __eq__(self, pawn):
        return self.position.location == pawn.position.location

    def temp_copy(self, position):
        '''Create new pawn from current pawn with updated position

        Parameters:
            position (Tile): New Position
        
        Returns:
            Pawn: New Pawn with updated position
        '''
        temp_pawn = Pawn(self.id, position, self.color)
        temp_pawn.has_red = self.has_red
        temp_pawn.has_green = self.has_green
        temp_pawn.has_neutral = self.has_neutral

        return temp_pawn
    
    def copy(self, pawn):
        '''Copy Pawn
        
        Parameters:
            pawn (Pawn): Destination Pawn
        '''
        self.position = pawn.position
        self.has_red = pawn.has_red
        self.has_green = pawn.has_green
        self.has_neutral = pawn.has_neutral