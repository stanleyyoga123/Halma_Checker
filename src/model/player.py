from .color import Color

class Player():
    '''Player contains atribute for each player
    '''
    def __init__(self, brain):
        '''Constructor
        
        Parameters:
            brain(Brain) : Brain injected for the player
        '''
        self.brain = brain

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
    
    def get_destination(self, color):
        return (0,0) if color == Color.GREEN else (self.state.board.b_size-1, self.state.board.b_size-1)