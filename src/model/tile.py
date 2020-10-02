class Tile():
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.location = (row, col)
        self.color = color
    
    def __str__(self):
        return f'({self.row},{self.col})'