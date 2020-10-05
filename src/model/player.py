class Player():
    '''Player contains atribute for each player
    '''
    def __init__(self, brain):
        '''Constructor
        
        Parameters:
            brain(Brain) : Brain injected for the player
        '''
        self.brain = brain
        
    def __repr__(self):
        return self.brain.__repr__()

    def inject(self, pawns, color, winCondition):
        '''Dependencies Injection Procedure

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
    
    