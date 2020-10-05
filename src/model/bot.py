from .player import Player
from .state import State

class Bot(Player):
    '''Bot inherit from Player.
    It's bot AI.
    '''

    def __init__(self, brain):
        '''Constructor

        Parameters:
            pawns (list(Pawn)): Bot pawns
            color (int): Agents color
            winCondition (list(Tile)): Tiles needed for agent to win
            t_limit (int): Time limit agent for thinking
        '''
        super().__init__(brain)
    
    def inject(self, pawns, color, winCondition, t_limit):
        super().inject(pawns, color,winCondition)
        self.t_limit = t_limit

    def find(self, state):
        return self.brain.find_best_move(state)
    