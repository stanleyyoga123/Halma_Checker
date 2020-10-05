from .brain import Brain
from src.constant import Constant
from src.utility import Utility

class MinimaxLocalSearch(Brain):
    '''Class that implemented Minimax algorithm with local search usage for finding best move in Brain class implementation
    '''
    def find_best_move(self, state):
        '''Find best move with minimax + local search
        
        Parameters:
            state (State): Current Game State
        
        Returns:
            State: Next state with best move being done by AI 
        '''
        print(Utility.utility_function(state))
        # raise NotImplementedError

    def __repr__(self):
        return Constant.MINMAXWLOCAL