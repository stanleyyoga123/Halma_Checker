from .pawn import Pawn
from .tile import Tile
from .color import Color    

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
                is_pawn = False
            out += '\n'
        return out

    def get_pawn(self, location):
        '''
        location = tuple(int, int)
        '''
        for pawn in self.pawns:
            if pawn.position.location == location:
                return pawn
        return None

    def check_tile_condition(self, before, after):
        '''
        before: Pawn
        after: Pawn
        '''
        return ((before.has_red and before.has_neutral and after.has_red and not after.has_neutral) or
                (before.has_green and before.has_neutral and after.has_red and not after.has_neutral) or
                (before.has_red and not before.has_neutral and after.has_green and not after.has_neutral) or
                (before.has_green and not before.has_neutral and after.has_red and not after.has_neutral))
    
    def is_out_board(self, location):
        '''
        location: tuple(int, int)
        '''
        return (location[0] >= self.b_size or location[1] >= self.b_size or location[0] < 0 or location[1] < 0)
        
    def check_move(self, pawn, direction):
        '''
        pawn: Pawn
        direction: String
        '''
        can_jump = False
        can_move = False
        updated_pawn_location = (pawn.position.location[0] + self.list_direction[direction][0],
                                pawn.position.location[1] + self.list_direction[direction][1])

        if not self.is_out_board(updated_pawn_location):
            if self.get_pawn(updated_pawn_location) is None:
                can_move = True
            else:
                updated_pawn_location = (updated_pawn_location[0] + self.list_direction[direction][0], 
                                        updated_pawn_location[1] + self.list_direction[direction][1])
                if self.get_pawn(updated_pawn_location) is None and not self.is_out_board(updated_pawn_location):
                    can_move = True
                    can_jump = True
                    temp_pawn = pawn.temp_copy(position=self.tiles[updated_pawn_location[0]][updated_pawn_location[1]])
                    temp_pawn = self.change_color_pawn(temp_pawn, self.tiles[updated_pawn_location[0]][updated_pawn_location[1]])

        if can_jump:
            return (can_move, can_jump, temp_pawn)
        else:
            return (can_move, can_jump, None)

    def possible_jump(self, pawn, history):
        '''
        pawn: Pawn
        history: Array
        '''
        for key, _ in self.list_direction.items():
            _, can_jump, pawn_after = self.check_move(pawn, key)
            if can_jump and pawn_after not in history:
                if self.check_tile_condition(pawn, pawn_after):
                    continue
                history.append(pawn_after)
                history = self.possible_jump(pawn_after, history)
        return history  
    
    def adjacent_move(self, pawn):
        '''
        pawn: Pawn
        '''
        possible_move = []
        for _, val in self.list_direction.items():
            updated_pawn_location = (pawn.position.location[0] + val[0],
                                    pawn.position.location[1] + val[1])
            
            if self.get_pawn(updated_pawn_location) is None and not self.is_out_board(updated_pawn_location):
                temp_pawn = pawn.temp_copy(position=self.tiles[updated_pawn_location[0]][updated_pawn_location[1]])
                temp_pawn = self.change_color_pawn(temp_pawn, self.tiles[updated_pawn_location[0]][updated_pawn_location[1]])
                possible_move.append(temp_pawn)
        
        return possible_move
    
    def change_color_pawn(self, pawn, tile):
        '''
        pawn: Pawn
        tile: Tile
        '''
        if tile.color == Color.RED:
            pawn.has_red = True
        elif tile.color == Color.GREEN:
            pawn.has_green = True
        else:
            pawn.has_neutral = True
        return pawn

    def possible_moves(self, pawn):
        '''
        pawn: Pawn
        '''
        adjacent_move = self.adjacent_move(pawn)
        jump_move = self.possible_jump(pawn, [])
        return adjacent_move + jump_move

    def move_pawn(self, before, after):
        '''
        before, after: Pawn
        '''
        print(before.position)
        print(after.position)
        for i, pawn in enumerate(self.pawns):
            if pawn == before:
                self.pawns[i].copy(after)