class Player():
    def __init__(self, pawns, color, winCondition):
        self.pawns = pawns
        self.color = color
        self.winCondition = winCondition

    def __eq__(self, player):
        return self.color == player.color