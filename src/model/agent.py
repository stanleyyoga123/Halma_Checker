from .player import Player
from .color import Color
from .utility import Utility
from .state import State

class Agent(Player):
    '''Agent inherit from Player.
    It's bot AI.
    '''

    def __init__(self, pawns, color, winCondition, t_limit):
        '''Constructor

        Parameters:
            pawns (list(Pawn)): Agents pawns
            color (int): Agents color
            winCondition (list(Tile)): Tiles needed for agent to win
            t_limit (int): Time limit agent for thinking
        '''
        super().__init__(pawns, color, winCondition)
        self.t_limit = t_limit
        self.state = None

    def utility_function(self, player):
        '''Utility Function for minimax algorithm

        Paramters:
            player (Player): Current Player

        Returns:
            int: Cost state 
        '''
        if player.color == Color.GREEN:
            destination = (0,0)
        else:
            destination = (self.state.board.b_size-1, self.state.board.b_size-1)
        
        cost = 0
        for pawn in player.panws:
            cost += Utility.distance(pawn.position.location, destination)
        
        if self.state.currentPlayer == player:
            cost *= -1
        
        return cost