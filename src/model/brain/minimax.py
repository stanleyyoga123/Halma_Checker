from .brain import Brain
from src.constant import Constant
from src.utility import Utility
from time import time
import random

class Minimax(Brain):
    '''Class that implemented Minimax algorithm for finding best move in Brain class implementation
    '''
     
    def minimax(self, state, is_max, depth = 0, alpha=float("-inf"), beta=float("inf")):
        """Minimax Algorithm for solving Halma Checker

        Parameters:
            state (State): game state
            is_max (Boolean): is maxing the objective value

        Returns:
            Tuple: Tuple of (state objective value, state)
        """
        # Terminate        
        if self.terminate(depth, state):
            return None, Utility.utility_function(state)        
        
        # Recursive
        possible_moves = state.current_player_possible_moves()
        temp_state = state.deepcopy()
        best_move = None
        best_move_val = float('-inf') if is_max else float('inf')
        
        for move in possible_moves:
            for to in move['to']:
                
                if time() > self.thinking_time:
                    # print("TIMEOUT")
                    return best_move, best_move_val
                
                temp_state.board.move_pawn(move['from'], to)
                temp_state.next_turn()
                _, val = self.minimax(temp_state, not(is_max), depth+1, alpha, beta)
                
                temp_state.board.move_pawn(to, move['from'])
                temp_state.undo_turn()
                
                if is_max and val > best_move_val:
                    best_move_val = val
                    best_move = (move['from'], to)
                    alpha = max(val, alpha)
                
                if not(is_max) and val < best_move_val:
                    best_move_val = val
                    best_move = (move['from'], to)
                    beta = min(val, beta)
                
                if beta <= alpha: #pruning
                    # print("PRUNING", best_move, best_move_val)
                    return best_move, best_move_val
                
        # print("LANCAR", best_move, best_move_val)
        return best_move, best_move_val

    def __repr__(self):
        return Constant.MINIMAX