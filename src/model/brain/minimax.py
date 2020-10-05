from .brain import Brain
from src.constant import Constant

class Minimax(Brain):
    '''Class that implemented Minimax algorithm for finding best move in Brain class implementation
    '''
    def find_best_move(self, state):
        '''Find best move with minimax algorithm
        
        Parameters:
            state (State): Current Game State
        
        Returns:
            State: Next state with best move being done by AI 
        '''
        raise NotImplementedError

    def __repr__(self):
        return Constant.MINIMAX