from .model.player import Player
from .model.board import Board 
from .model.agent import Agent
from .model.tile import Tile 
from .model.color import Color
from .model.pawn import Pawn

from .io.cli_input import CLIInput
from .io.cli_output import CLIOutput

class Halma():

    def __init__(self, b_size, t_limit, h_player):
        '''
        b_size = board size (8, 10, 16)
        t_limit = time limit
        h_player = player color
        '''
        self.inputter = CLIInput()    # inject dependencies for input 
        self.outputter = CLIOutput()  # inject dependencies for output

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
        tiles = [[Tile(i, j, Color.NEUTRAL) for j in range(b_size)] for i in range(b_size)]
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
            self.player_1 = Player(green['pawns'], Color.GREEN, green['win_condition'])
            self.player_2 = Agent(red['pawns'], Color.RED, red['win_condition'], t_limit)

        # History
        self.history = []

        # Current Player
        if h_player == Color.GREEN:
            self.currentPlayer = self.player_1
        else:
            self.currentPlayer = self.player_2

    def move(self):
        before, after = self.inputter.input(self.board, self.currentPlayer) 
        # TODO : move logic abis itu ... 
        self.board.move_pawn(before, after)

    def game(self):
        self.move()
        self.outputter.show(self.board)

        if self.currentPlayer == self.player_1:
            self.currentPlayer = self.player_2
        else:
            self.currentPlayer = self.player_1