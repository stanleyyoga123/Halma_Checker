from abc import ABCMeta, abstractmethod
from time import time

class Brain(metaclass=ABCMeta):
    '''Base class of brain for the AI implemented in Halma Game
    '''
    
    def reset(self):
        """Reset attributes
        """
        self.thinking_time = time() + self.t_limit
    
    def inject(self, t_limit):
        self.t_limit = t_limit
    
    @abstractmethod
    def find_best_move(self, state, max_depth = 3):
        '''Find best move
        
        Parameters:
            utility_function (func): Function for getting utility value
            state (State): Current Game State
        
        Returns:
            State: Next state with best move being done by AI 
        '''
        raise NotImplementedError
