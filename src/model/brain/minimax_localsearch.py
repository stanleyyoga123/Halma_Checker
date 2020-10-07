from .brain import Brain
from src.constant import Constant
from src.utility import Utility
from time import time

class MinimaxLocalSearch(Brain):
    '''Class that implemented Minimax algorithm with local search usage for finding best move in Brain class implementation
    '''
    
    def terminate(self, depth, state):
        p1_win, p2_win = state.win_condition()
        return depth == 0 or p1_win or p2_win or time() > self.thinking_time
    
    def max_value(self, state, depth):
        # Terminate        
        if self.terminate(depth, state):
            return None, Utility.utility_function(state)
        
        # Recursive
        best_move = None
        best_move_val = float('-inf')
        possible_moves = state.current_player_possible_moves()
        temp_state = state.deepcopy()
        
        for move in possible_moves:
            for to in move['to']:
                if time() > self.thinking_time:
                    return best_move, best_move_val
                
                temp_state.board.move_pawn(move['from'], to)
                temp_state.next_turn()
                _, val = self.min_value(temp_state, depth-1)
                
                temp_state.board.move_pawn(to, move['from'])
                
                if val > best_move_val:
                    best_move_val = val
                    best_move = (move['from'], to)
                    self.alpha = max(val, self.alpha)

                if self.pruning():
                    return best_move, best_move_val 
                    
        return best_move, best_move_val
        
    def min_value(self, state, depth):
        if self.terminate(depth, state):
            return None, Utility.utility_function(state)
        
        # Recursive
        best_move = None
        best_move_val = float('inf')
        possible_moves = state.current_player_possible_moves()
        temp_state = state.deepcopy()
        
        for move in possible_moves:
            for to in move['to']:
                if time() > self.thinking_time:
                    return best_move, best_move_val
                
                temp_state.board.move_pawn(move['from'], to)
                temp_state.next_turn()
                _, val = self.max_value(temp_state, depth-1)
                
                temp_state.board.move_pawn(to, move['from'])
                
                if val < best_move_val:
                    best_move_val = val
                    best_move = (move['from'], to)
                    self.beta = min(val, self.beta)

                if self.pruning():
                    return best_move, best_move_val 
                    
        return best_move, best_move_val
     
    def minimax(self, state, is_max, depth):
        """Minimax Algorithm for solving Halma Checker

        Parameters:
            state (State): game state
            is_max (Boolean): is maxing the objective value

        Returns:
            Tuple: Tuple of (state objective value, state)
        """
        return self.max_value(state, depth) if is_max else self.min_value(state, depth) 
    
    def pruning(self):
        """Prunning in Minimax Algorithm

        Returns:
            Boolean: True if beta <= alpha
        """
        return self.beta <= self.alpha
    
    def find_best_move(self, state, max_depth = 1):
        '''Find best move with minimax + local search
        
        Parameters:
            state (State): Current Game State
        
        Returns:
            State: Next state with best move being done by AI 
        '''
        self.reset()
        best_moves, _ = self.minimax(state, state.currentPlayer == state.player_2, max_depth)
        return best_moves

    def __repr__(self):
        return Constant.MINMAXWLOCAL