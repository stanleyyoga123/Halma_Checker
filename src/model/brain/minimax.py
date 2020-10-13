from .brain import Brain
from src.constant import Constant
from src.utility import Utility
from time import time
import random

class Minimax(Brain):
    '''Class that implemented Minimax algorithm for finding best move in Brain class implementation
    '''

    def terminate(self, depth, state):
        p1_win, p2_win = state.win_condition()
        if time() > self.thinking_time: print("TIME'S UP")
        return depth == self.max_depth or p1_win or p2_win or time() > self.thinking_time
     
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
                    print("TIMEOUT")
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
    
    def find_best_move(self, state, max_depth = 3):
        '''Find best move with minimax + local search
        
        Parameters:
            state (State): Current Game State
        
        Returns:
            State: Next state with best move being done by AI 
        '''
        self.reset()
        self.max_depth = max_depth
        best_moves, _ = self.minimax(state, state.currentPlayer == state.player_2)
        if best_moves == None:
            possible_moves = state.current_player_possible_moves()
            move = random.choice(list(possible_moves))
            move_to_random = random.choice(list(move['to']))
            return (move['from'], move_to_random)
        return best_moves

    def __repr__(self):
        return Constant.MINIMAX