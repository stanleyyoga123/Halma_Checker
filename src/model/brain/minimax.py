from .brain import Brain
from src.constant import Constant

class Minimax(Brain):
    '''Class that implemented Minimax algorithm for finding best move in Brain class implementation
    '''
    def find_best_move(self, utility_function, state):
        raise NotImplementedError

    def __repr__(self):
        return Constant.MINIMAX