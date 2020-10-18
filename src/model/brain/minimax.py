from .brain import Brain
from src.constant import Constant
from src.utility import Utility
from time import time

class Minimax(Brain):
    '''Class that implemented Minimax algorithm for finding best move in Brain class implementation
    '''
     
    def minimax(self, state, is_max, depth = 0, alpha=float("-inf"), beta=float("inf")):
        """Minimax Algorithm for solving Halma Checker

        Parameters:
            state (State): game state
            is_max (Boolean): is maxing the objective value

        Returns:
            Tuple: Tuple of (best_move objective value, best_move)
        """
        # Terminate        
        if self.terminate(depth, state):
            return None, Utility.utility_function(state)        
        
        # Recursive
        possible_moves = state.current_player_possible_moves()
        return self.search(is_max, possible_moves, state, depth, alpha, beta)
        
        
    def search(self, is_max, possible_moves, state, depth, alpha, beta):
        """Brain with Minimax search tree

        Args:
            is_max (bool): if player max
            possible_moves (list(dict(from, to))): List possible moves of current player
            state (State): current state
            depth (int): current depth
            alpha (float): alpha for alpha beta pruning
            beta (float): beta for alpha beta pruning

        Returns:
            Tuple: Tuple of (best_move objective value, best_move)
        """
        temp_state = state.deepcopy()
        best_move = None
        best_move_val = float('-inf') if is_max else float('inf')
        
        for move in possible_moves:
            for to in move['to']:
                
                if time() > self.thinking_time:
                    return best_move, best_move_val
                
                temp_state.board.move_pawn(move['from'], to)
                temp_state.next_turn()
                _, val = self.minimax(temp_state, not(is_max), depth+1, alpha, beta)
                
                temp_state.board.move_pawn(to, move['from'])
                temp_state.undo_turn()
                
                if is_max and val > best_move_val:
                    alpha = max(val, alpha)
                    best_move_val = val
                    best_move = (move['from'], to)
                
                if not(is_max) and val < best_move_val:
                    beta = min(val, beta)
                    best_move_val = val
                    best_move = (move['from'], to)
                
                if beta <= alpha: #pruning
                    return best_move, best_move_val
                
        return best_move, best_move_val

    def __repr__(self):
        return Constant.MINIMAX