class Utility():
    '''Class for general function that can be used on all class
    '''
    @staticmethod
    def distance(coordinate, destination):
        '''Given two point, find the euclidean distance

        Parameters:
            coordinate (tuple(int, int)): Given Point
            destination (tuple(int, int)): Destination
        
        Returns:
            int: Euclidean Distance
        '''
        euclidean = 0
        for d_coordinate, d_destination in zip(coordinate, destination):
            euclidean += (d_coordinate - d_destination) ** 2
        euclidean = euclidean ** (0.5)

        return euclidean
    
    @staticmethod
    def utility_function(state):
        '''Utility Function for minimax algorithm

        Paramters:
            state: current state

        Returns:
            int: Cost state 
        '''
        current_player = state.currentPlayer
        destination = state.board.get_destination(current_player.color)
        
        cost = 0
        for pawn in current_player.pawns:
            cost += Utility.distance(pawn.position.location, destination)
        
        if current_player == state.player_1: #Jika Bot
            cost *= -1
        
        return cost