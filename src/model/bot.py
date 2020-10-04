from .player import Player
from .state import State
from src.utility import Utility

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
        self.state = None
    
    def inject(self, pawns, color, winCondition, t_limit):
        super().inject(pawns, color,winCondition)
        self.t_limit = t_limit

    def utility_function(self, player):
        '''Utility Function for minimax algorithm

        Paramters:
            player (Player): Current Player

        Returns:
            int: Cost state 
        '''
        destination = self.get_destination(player.color)
        
        cost = 0
        for pawn in player.panws:
            cost += Utility.distance(pawn.position.location, destination)
        
        if self.state.currentPlayer == player:
            cost *= -1
        
        return cost

    def find(self, state):
        return self.brain.find_best_move(self.utility_function, self.state)
    