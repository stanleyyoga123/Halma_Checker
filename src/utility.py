from src.model.tile import Tile

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
            # print(Utility.distance(pawn.position.location, destination))
            cost -= Utility.distance(pawn.position.location, destination)
            # print(pawn.position, pawn.position != Tile(0,0,1))
            
        for pawn in opponent_player.pawns:
            cost += Utility.distance(pawn.position.location, destination)
        
        if current_player == state.player_2: #Jika Human
            cost *= -1
        
        return cost
    
    # @staticmethod
    # def utility_function(state):
    #     '''Utility Function for minimax algorithm

    #     Paramters:
    #         state: current state

    #     Returns:
    #         int: Cost state 
    #     '''
    #     current_player = state.currentPlayer
    #     opponent_player = state.opponent_player()
        
    #     cost = 100
    #     for pawn in current_player.pawns:
    #         possible_value = [Utility.distance(pawn.position.location, dest.location) for dest in current_player.winCondition
    #                           if pawn.position != dest]
    #         cost -= max(possible_value) if len(possible_value) else 0
            
    #     for pawn in opponent_player.pawns:
    #         possible_value = [Utility.distance(pawn.position.location, dest.location) for dest in opponent_player.winCondition
    #                           if pawn.position != dest]
    #         cost += max(possible_value) if len(possible_value) else 0
        
    #     if current_player == state.player_2: #Jika Human
    #         cost *= -1
    #         print("MASOOOK A", cost)
        
    #     return cost