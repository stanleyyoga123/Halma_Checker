from .brain import Brain
from src.constant import Constant
from src.utility import Utility
from time import time
from random import randint
from math import exp

class MinimaxLocalSearch(Brain):
    '''Class that implemented Minimax algorithm with local search usage for finding best move in Brain class implementation
    '''
    
    def generate_random_move(self, possible_moves):
        """Generate random move from array of possible_moves

        Args:
            possible_moves (list(dict(from, to))): List possible moves of current player

        Returns:
            dict(from, to): Dictionary of from and to
        """
        rand_idx = randint(0, len(possible_moves)-1) if len(possible_moves) > 1 else -1
        selected_move = possible_moves[rand_idx]
        if len(selected_move['to']) > 1:
            selected_move['to'] = [selected_move['to'].pop()] 
        else:            
            possible_moves.pop(rand_idx)
        return selected_move if selected_move and len(selected_move['to']) else None, possible_moves
    
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
        
        # print(possible_moves)
        if self.which_player == state.currentPlayer: 
            # Jika giliran bot player, maka jalankan localsearch untuk mengambil beberapa possible moves saja
            possible_moves = self.local_search(temp_state, possible_moves)
            
        #Jika bukan bot, pertimbangkan semua moves
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
                # print("RECCC VAL", val)
                
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
                
                if beta <= alpha:
                    return best_move, best_move_val
        
        return best_move, best_move_val
    
    def local_search(self, current_state, possible_moves):
        """Local search using Simulated Annealing Algorithm

        Args:
            current_state (State): Current state
            possible_moves (list(dict(from, to))): List possible moves of current player
            depth (int): Depth

        Returns:
            (list(dict(from, to))): new possible_moves with less possible moves
        """
        #1/5 dari batas waktu setiap depth (asumsi waktu alokasi tiap depth uniform, 
        # dan butuh 4/5 waktu untuk menelusuri pohon) 
        sa_time = time() + self.t_limit/(self.max_depth*5)
        generated_moves = []
        while True:
            curr_time = sa_time - time()
            if curr_time <= 0 or not possible_moves: return generated_moves
            next_move, possible_moves = self.generate_random_move(possible_moves)
            # temp_state = current_state.deepcopy()
            # current_state.board.move_pawn(next_move['from'], next_move['to'][0])
            if next_move:
                delta_e = Utility.distance(next_move['to'][0].position.location, current_state.board.get_destination(current_state.currentPlayer.color)) - Utility.distance(next_move['from'].position.location, current_state.board.get_destination(current_state.currentPlayer.color))
                # current_state.board.move_pawn(next_move['to'][0], next_move['from'])
                if delta_e > 0.5: generated_moves.append(next_move)
                elif exp(delta_e/curr_time): generated_moves.append(next_move)
                # print("DELTA E", exp(delta_e/curr_time))
            
    def find_best_move(self, state, max_depth = 3):
        '''Find best move with minimax + local search
        
        Parameters:
            state (State): Current Game State
        
        Returns:
            State: Next state with best move being done by AI 
        '''
        self.reset()
        self.max_depth = max_depth
        self.which_player = state.currentPlayer
        best_moves, _ = self.minimax(state, state.currentPlayer == state.player_2)
        return best_moves

    def __repr__(self):
        return Constant.MINMAXWLOCAL