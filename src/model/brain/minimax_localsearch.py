from .brain import Brain
from src.constant import Constant

class MinimaxLocalSearch(Brain):
    '''Class that implemented Minimax algorithm with local search usage for finding best move in Brain class implementation
    '''
    def find_best_move(self, utility_function, state):
        raise NotImplementedError

    def __repr__(self):
        return Constant.MINMAXWLOCAL