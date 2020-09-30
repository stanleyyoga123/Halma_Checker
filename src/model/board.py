class Board():
    def __init__(self, b_size, pawns, tiles):
        self.b_size = b_size
        self.pawns = pawns
        self.tiles = tiles

    def __str__(self):
        out = ''
        is_pawn = False
        for i in range(self.b_size):
            for j in range(self.b_size):
                # Find pawn in tiles
                for pawn in self.pawns:
                    if pawn.position.location == (i,j):
                        is_pawn = True
                        out += pawn.__str__()
                if not is_pawn:
                    out += ' '
                is_pawn = False
            out += '\n'
        return out
