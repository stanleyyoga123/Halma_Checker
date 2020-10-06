from .brain import Brain
from src.constant import Constant
from src.utility import Utility
from time import time

class MinimaxLocalSearch(Brain):
    '''Class that implemented Minimax algorithm with local search usage for finding best move in Brain class implementation
    '''         
    def minimax(self, state, is_max):
        """Minimax Algorithm for solving Halma Checker

        Parameters:
            state (State): game state
            is_max (Boolean): is maxing the objective value

        Returns:
            Tuple: Tuple of (state objective value, state)
        """
        if (self.depth == 0) or state.win_condition() or time() > self.thinking_time:
            return (Utility.utility_function(state), state)

        if is_max:
            max_eval = float('-inf')
            best_state = None
    
    def find_best_move(self, state):
        '''Find best move with minimax + local search
        
        Parameters:
            state (State): Current Game State
        
        Returns:
            State: Next state with best move being done by AI 
        '''
        self.reset()
        new_state = self.minimax(state, state.currentPlayer == state.player_2)
        return state, new_state

    def __repr__(self):
        return Constant.MINMAXWLOCAL