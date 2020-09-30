from src.model.player import Player
from src.model.board import Board 
from src.model.agent import Agent
from src.model.tile import Tile 
from src.model.color import Color


class Halma():

    def __init__(self, b_size, t_limit, h_player):
        '''
        b_size = board size (8, 10, 16)
        t_limit = time limit
        h_player = player color
        '''
        self.turn = 0
        self.t_limit = t_limit

        cur_id = 0
        red = {
            'pawns': [],
            'win_condition': [],
        }
        green = {
            'pawns': [],
            'win_condition': [],
        }

        # Create all tiles to neutral
        tiles = [[Tile(i, j, Color.NEUTRAL) for i in range(b_size)] for j in range(b_size)]
        
        # Red Location
        for i in range(4):
            for j in range(4-i):
                # Change Tile color to red
                tiles[i][j].color = Color.RED
                # Add win condition for green
                red['win_condition'].append(tiles[i][j])
                # Add red pawn to list
                red['pawns'].append(Pawn(cur_id, tiles[i][j], Color.RED))  
                cur_id += 1

        # Green Location
        count = 1
        for i in range(b_size-count, b_size-5, -1):
            for j in range(b_size-1, b_size+count-6, -1):
                # Change Tile color to green
                tiles[i][j].color = Color.GREEN
                # Add win condition for red
                green['win_condition'].append(tiles[i][j])
                # Add green pawn to list
                green['pawns'].append(Pawn(cur_id, tiles[i][j], Color.GREEN))
                cur_id += 1
            count += 1

        # Initialize Board
        all_pawns = red['pawns'] + green['pawns']
        self.board = Board(b_size, all_pawns, tiles)

        # Initialize Player
        if h_player == Color.RED:
            self.player_1 = Player(red['pawns'], Color.RED, red['win_condition'])
            self.player_2 = Agent(green['pawns'], Color.GREEN, green['win_condition'], t_limit)
        else:
            self.player_1 = Player(red['pawns'], Color.RED, red['win_condition'])
            self.player_2 = Agent(green['pawns'], Color.GREEN, green['win_condition'], t_limit)

        # History
        self.history = []

        # Current Board
        self.currentBoard = None

if __name__ == '__main__':
    game = Halma(10, 10, Color.RED)
    print(game.board)