from .player import Player

class Agent(Player):

    def __init__(self, pawns, color, winCondition, t_limit):
        super().__init__(pawns, color, winCondition)
        self.t_limit = t_limit