from .model.player import Player
from .model.board import Board 
from .model.bot import Bot
from .model.tile import Tile 
from .model.color import Color
from .model.pawn import Pawn
from .model.state import State
from .constant import Constant

class Halma():
    '''Halma class responsible for controlling flow in the game
    '''
    def __init__(self, b_size, t_limit, h_player, interface, player1, player2):
        '''Constructor

        Parameters:
            b_size (int): Board size
            t_limit (int): Time limit
            h_player (int): Player color
            interface (I/O Interface): I/O for game
            player1 (Player): Player Object representing player 1
            player2 (Player): Player Object representing player 2
        '''
        # Initialize properties
        self.interface = interface 

        self.t_limit = t_limit
        self.b_size = b_size
        self.h_player = h_player

        # Initialize game location
        red, green, tiles = self.init_location()

        # Initialize Board
        board = Board(b_size, red['pawns'] + green['pawns'], tiles)

        # Init player
        player_1, player_2 = self.init_player(red, green, player1, player2)

        # History
        self.history = []

        # Current Player        
        currentPlayer = player_1 if player_1.color == Color.GREEN else player_2

        # State
        self.state = State(board, player_1, player_2, currentPlayer)

        # game over state
        self.game_over = False

    def move(self):
        '''Method to move pawn
        '''
        if repr(self.state.currentPlayer.brain) == Constant.NOBRAIN:
            before, after = self.interface.input(self.state) 
            self.state.board.move_pawn(before, after)
        else :
            before, after = self.state.currentPlayer.find(self.state)
            # print(before.__repr__(), after.__repr__())
            self.state.board.move_pawn(before, after)

    def game(self):
        '''Main method for each turn
        '''
        if repr(self.state.currentPlayer.brain) != Constant.NOBRAIN:
            self.state.currentPlayer.state = self.state

        # assertion to check if the game not over yet
        if self.game_over:
            return

        self.move()

        if(self.state.win_condition()[0] or self.state.win_condition()[1]):
            self.game_over = True
            self.interface.show_winner(self.state.currentPlayer)
        else : 
            self.next()

        self.interface.render(self.state)
    
    def next(self):
        '''Updating attribute after turn end
        '''
        self.history.append(self.state.deepcopy())
        self.state.next_turn()
        # self.state.update(self.board, self.state.player_1, self.state.player_2, self.currentPlayer, self.turn)
    
    def init_player(self, red, green, player1, player2):
        '''Initialize Player
        
        Parameters:
            red (dict): Red player
            green (dict): Green player
            player1 (Player): Player Object representing player 1
            player2 (Player): Player Object representing player 2
        
        Returns:
            Tuple(Player, Player: Initialized Player
        '''
        def closure_init_player(setup, color, player, t_limit):
            if repr(player.brain) == Constant.NOBRAIN:
                player.inject(setup.get('pawns'), color, setup.get('win_condition'))
            else: 
                player.inject(setup.get('pawns'), color, setup.get('win_condition'), t_limit)
            return player

        reverse_color = Color.GREEN if Color.RED == self.h_player else Color.RED
        first_setup = green if reverse_color == Color.GREEN else red 
        second_setup = green if reverse_color == Color.RED else red


        player1 = closure_init_player(first_setup, reverse_color, player1, self.t_limit)
        player2 = closure_init_player(second_setup, self.h_player, player2, self.t_limit)
        return (player1, player2)

    def init_location(self):
        '''Initialize all location (tiles, winCondition, etc) for green, red, and board

        Returns:
            Tuple(map, map, list(Tile)): Initialized Location
        '''
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
        tiles = [[Tile(i, j, Color.NEUTRAL) for j in range(self.b_size)] for i in range(self.b_size)]

        # Red Location
        for i in range(4):
            for j in range(4-i):
                # Change Tile color to red
                tiles[i][j].color = Color.RED
                # Add win condition for green
                green['win_condition'].append(tiles[i][j])
                # Add red pawn to list
                red['pawns'].append(Pawn(cur_id, tiles[i][j], Color.RED))  
                cur_id += 1

        # Green Location
        count = 1
        for i in range(self.b_size-count, self.b_size-5, -1):
            for j in range(self.b_size-1, self.b_size+count-6, -1):
                # Change Tile color to green
                tiles[i][j].color = Color.GREEN
                # Add win condition for red
                red['win_condition'].append(tiles[i][j])
                # Add green pawn to list
                green['pawns'].append(Pawn(cur_id, tiles[i][j], Color.GREEN))
                cur_id += 1
            count += 1

        return red, green, tiles
