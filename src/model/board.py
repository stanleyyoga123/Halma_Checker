from .pawn import Pawn
from .tile import Tile
from .color import Color

from colorama import Fore, Style

class Board():
    def __init__(self, b_size, pawns, tiles):
        self.b_size = b_size
        self.pawns = pawns
        self.tiles = tiles
        self.list_direction = {
            'UP': (-1, 0),
            'DOWN': (1, 0),
            'LEFT': (0, -1),
            'RIGHT': (0, 1),
            'DIAGONAL-RIGHT-UP': (-1, 1),
            'DIAGONAL-RIGHT-DOWN': (1, 1),
            'DIAGONAL-LEFT-UP': (-1, -1),
            'DIAGONAL-LEFT-DOWN': (1, -1)
        }

    def __str__(self):
        out = ''
        is_pawn = False
        for i in range(self.b_size):
            for j in range(self.b_size):
                # Find pawn in tiles
                for pawn in self.pawns:
                    if pawn.position.location == (i,j):
                        is_pawn = True
                        out += pawn.__str__()
                if not is_pawn:
                    out += '.'
                out += ' '
                is_pawn = False
            out += '\n'
        return out

    def get_pawn(self, location):
        '''Find pawn based on their location in board

        Parameters:
            location (Tuple(int, int)): Location Pawn

        Returns:
            Pawn: Pawn Founds
        '''
        for pawn in self.pawns:
            if pawn.position.location == location:
                return pawn
        return None

    def base_field_checker(self, pawn, after):
        '''Check if pawn move back to its base, or 
        move out from enemy base

        Parameters:
            pawn (Pawn): Selected Pawn 
            after (Tile): Destination Tile

        Returns:
            boolean: True if they move back to its base or move out from enemy base  
        '''
        neutral_to_base = (pawn.has_red and pawn.has_neutral and after.color == Color.RED) or \
                            (pawn.has_green and pawn.has_neutral and after.color == Color.GREEN)
        base_to_neutral = pawn.has_red and pawn.has_green and after.color == Color.NEUTRAL
        return neutral_to_base or base_to_neutral
    
    def is_out_board(self, destination):
        '''Check if destinations is out of board

        Parameters:
            destination (Tuple(int, int)): Destination Tiles 

        Returns:
            boolean: True if destination is out of board
        '''
        return (destination[0] >= self.b_size or destination[1] >= self.b_size or destination[0] < 0 or destination[1] < 0)
        
    def check_jump(self, pawn, direction):
        '''Check if pawn can jump in which direction

        Parameters:
            pawn (Pawn): Selected Pawn
            direction (String): Direction which pawn will jump
        
        Returns:
            boolean: True if pawn can jump
            Pawn: Temporary Pawn with location after jumping
        '''
        can_jump = False
        updated_pawn_location = (pawn.position.location[0] + self.list_direction[direction][0],
                                pawn.position.location[1] + self.list_direction[direction][1])

        if not self.is_out_board(updated_pawn_location):
            if self.get_pawn(updated_pawn_location) is not None:
                updated_pawn_location = (updated_pawn_location[0] + self.list_direction[direction][0], 
                                        updated_pawn_location[1] + self.list_direction[direction][1])
                if (self.get_pawn(updated_pawn_location) is None) and \
                        (not self.is_out_board(updated_pawn_location)):
                    can_jump = True
                    temp_pawn = pawn.temp_copy(position=self.tiles[updated_pawn_location[0]][updated_pawn_location[1]])
                    temp_pawn = self.change_color_pawn(temp_pawn, self.tiles[updated_pawn_location[0]][updated_pawn_location[1]])

        if can_jump:
            return (can_jump, temp_pawn)
        else:
            return (can_jump, None)

    def possible_jump(self, pawn, history):
        '''Get all possibility jump from selected pawn

        Parameters:
            pawn (Pawn): Selected Pawn
            history (Array(Pawn)): History jump from selected Pawn
        
        Returns:
            Array(Pawn): List of possibility jump from selected Pawn
        '''
        for key, _ in self.list_direction.items():
            can_jump, pawn_after = self.check_move(pawn, key)
            if can_jump and pawn_after not in history:
                if self.base_field_checker(pawn, pawn_after.position):
                    continue
                history.append(pawn_after)
                history = self.possible_jump(pawn_after, history)
        return history  
    
    def adjacent_move(self, pawn):
        '''Get all possibiliy adjacent moves from selected Pawn

        Parameters:
            pawn (Pawn): Selected Pawn

        Returns:
            Array(Pawn): List of possibiliy adjacent moves from selected Pawn
        '''
        possible_move = []
        for _, val in self.list_direction.items():
            updated_pawn_location = (pawn.position.location[0] + val[0],
                                    pawn.position.location[1] + val[1])

            if self.get_pawn(updated_pawn_location) is None and not self.is_out_board(updated_pawn_location):
                if (self.base_field_checker(pawn, self.tiles[updated_pawn_location[0]][updated_pawn_location[1]])):
                    continue
                temp_pawn = pawn.temp_copy(position=self.tiles[updated_pawn_location[0]][updated_pawn_location[1]])
                temp_pawn = self.change_color_pawn(temp_pawn, self.tiles[updated_pawn_location[0]][updated_pawn_location[1]])
                possible_move.append(temp_pawn)
        
        return possible_move
    
    def change_color_pawn(self, pawn, tile):
        '''Change history of color tiles passed from pawn

        Parameters:
            pawn (Pawn): Selected Pawn
            tile (Tile): Tile where selected Pawn landed after move

        Returns:
            Pawn: Updated Pawn 
        '''
        if tile.color == Color.RED:
            pawn.has_red = True
        elif tile.color == Color.GREEN:
            pawn.has_green = True
        else:
            pawn.has_neutral = True
        return pawn

    def possible_moves(self, pawn):
        '''Get all possible moves from selected Pawn
        
        Parameters:
            pawn (Pawn): Selected Pawn
        
        Returns:
            Array(Pawn): List of possible moves from selected Pawn
        '''
        adjacent_move = self.adjacent_move(pawn)
        jump_move = self.possible_jump(pawn, [])
        return adjacent_move + jump_move

    def move_pawn(self, before, after):
        '''Update Pawn to new location

        Parameters:
            before (Pawn): Selected Pawn
            after (Pawn): Destination Pawn
        '''
        print(before.position)
        print(after.position)
        for i, pawn in enumerate(self.pawns):
            if pawn == before:
                self.pawns[i].copy(after)