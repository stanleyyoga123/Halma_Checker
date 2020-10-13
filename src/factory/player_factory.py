from src.model import Player, Bot
from src.model.brain import Minimax, MinimaxLocalSearch, NoBrain

from src.constant import Constant

class PlayerFactory():
    '''Class that act as factory for Player Class
    '''
    @staticmethod
    def generate_player(brain_type):
        '''Given brain type, return the correct type of brain

        Parameters:
            brain_type (str) : the representation of brain for player
         
        Returns:
            Player: Player based on the brain with AI logic (or not)
        '''
        if brain_type == Constant.NOBRAIN:
            return Player(NoBrain())
            return Bot(MinimaxLocalSearch())
        
        elif brain_type == Constant.MINIMAX:
            return Bot(Minimax())
        
        elif brain_type == Constant.MINMAXWLOCAL:
            return Bot(MinimaxLocalSearch())
        
        else : 
            raise ValueError()