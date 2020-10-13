import copy

class State():
    '''Class State contains state of current game
    '''
    def __init__(self, board, player_1, player_2, currentPlayer):
        '''Constructor

        Parameters:
            board (Board): Current Board state
            player_1 (Player): player_1 state
            player_2 (Player): player_2 state
            currentPlayer (Player): Current Player state
        '''
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.currentPlayer = currentPlayer
        self.turn = 0

    def opponent_player(self):
        return self.player_1 if self.currentPlayer == self.player_1 else self.player_2

    def update(self, board, player_1, player_2, currentPlayer, turn):
        '''Change State attribute
        
        Parameters:
            board (Board): Current Board state
            player_1 (Player): player_1 state
            player_2 (Player): player_2 state
            currentPlayer (Player): Current Player state
            turn (int): Current turn
        '''
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2
        self.currentPlayer = currentPlayer
        self.turn = turn
    
    def __str__(self):
        return self.board.__str__()
    
    def next_turn(self):
        self.currentPlayer = self.player_2 if self.currentPlayer == self.player_1 else self.player_1
        self.turn += 1
        
    def undo_turn(self):
        self.currentPlayer = self.player_2 if self.currentPlayer == self.player_1 else self.player_1
        self.turn -= 1

    def deepcopy(self):
        '''Copy State
        
        Returns:
            state (State): State
        '''

        # TODO: Need to deepcopy for all object parameter
        return copy.deepcopy(self)

    def win_condition(self):
        '''Winning condition for player

        Returns:
            Tuple(Boolean, Boolean): index represent player
        '''
        if(self.player_1.is_win()):
            return (True, False)
        elif(self.player_2.is_win()):
            return (False, True)
        else:
            return (False, False)
        
    def current_player_possible_moves(self):
        """Get all possible moves of current player

        Returns:
            List(dict(from: Pawn, to: List(Pawn))): list of dict of (pawn and list of possible moves that pawn)
        """
        return list((map(
            lambda pawn: {'from': pawn, 'to':self.board.possible_moves(pawn)}, 
            self.currentPlayer.pawns)))