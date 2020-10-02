class Player():
    '''Player contains atribute for each player
    '''
    def __init__(self, pawns, color, winCondition):
        '''Constructor
        
        Parameters:
            pawns (list(Pawn)): Players pawns
            color (int): Players color
            winCondition (list(Tile)): Tiles needed for player to win
        '''
        self.pawns = pawns
        self.color = color
        self.winCondition = winCondition

    def __eq__(self, player):
        return self.color == player.color