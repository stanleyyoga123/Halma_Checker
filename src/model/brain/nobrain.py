from .brain import Brain
from src.constant import Constant

class NoBrain(Brain):
    '''Class that not implemented any intelligence for finding best move in Brain class implementation
    '''
    def __init__(self):
        super().__init__()
    
    def find_best_move(self, state):
        '''No brain find best move (should not be implemented, as a representation only)
        
        Parameters:
            utility_function (func): Function for getting utility value
            state (State): Current Game State
        
        Returns:
            State: Next state with best move being done by AI 
        '''
        raise NotImplementedError

    def __repr__(self):
        return Constant.NOBRAIN