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
        opponent_player = state.player_1 if current_player == state.player_2 else state.player_2
        destination = state.board.get_destination(current_player.color)
        
        cost = 100
        for pawn in current_player.pawns:
            if pawn.position in current_player.winCondition:
                mult = 1
            else:
                mult = 0
            cost -= Utility.distance(pawn.position.location, destination) - mult
            
        for pawn in opponent_player.pawns:
            if pawn.position in opponent_player.winCondition:
                mult = 1
            else:
                mult = 0
            cost += Utility.distance(pawn.position.location, destination) + mult
        
        if current_player == state.player_2: #Jika Human
            cost *= -1
        
        return cost