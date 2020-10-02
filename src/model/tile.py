class Tile():
    '''Containts attribute for each tile used on board
    '''
    def __init__(self, row, col, color):
        '''Constructor

        Parameters:
            row (int): Tile row
            col (int): Tile column
            color (int): Tile color
        '''
        self.row = row
        self.col = col
        self.location = (row, col)
        self.color = color
    
    def __str__(self):
        return f'({self.row},{self.col})'