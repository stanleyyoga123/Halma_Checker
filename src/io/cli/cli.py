import pyfiglet	
from clint.arguments import Args
from clint.textui import puts, colored
from PyInquirer import style_from_dict, Token, prompt

from src.factory import PlayerFactory
from src.constant import Constant

from .utils import get_style
from ...model import Color

class CLI():
    def render(self, state, time=None):
        print ("Game Status : ")
        print(f"Current Player : {str(state.currentPlayer)}")
        print(f"Current Turn : {state.turn + 1}")
        print(f"Computing Time : {time if time != None else '-'} seconds\n")
        print(colored.green(str(state.board)))

    def input(self, state):
        found = False
        while not found:
            pawns = [f"Pawns at {pawn.position}" for pawn in state.currentPlayer.pawns]
            i_choosed_pawn = self.ask_pawn(pawns)
            choosed_pawn = state.currentPlayer.pawns[i_choosed_pawn]

            possible_moves = state.board.possible_moves(choosed_pawn)

            if len(possible_moves) <= 0:
                continue

            possible_moves_str = [f"Pawn to {pawn.position}" for pawn in possible_moves]
            i_moved_pawn = self.ask_movement(possible_moves_str)
            found = True

        moved_pawn = possible_moves[i_moved_pawn] 
        print(f'You Choose Pawn from {choosed_pawn.position} Move to {moved_pawn.position}')
        print()

        return (choosed_pawn, moved_pawn)

    def ask_movement(self, possible_moves):
        question = [
            {
                'type': 'list',
                'name': 'move',
                'message': 'Please choose a posible move : ',
                'choices': possible_moves,
                'filter': lambda val: possible_moves.index(val)
            }
        ]
        return prompt(question, style = style_from_dict(get_style()))['move']

    def ask_pawn(self, pawns):
        question = [
            {
                'type' : 'list',
                'name' : 'pawn',
                'message' : "Please choose a pawn to move : ",
                'choices' : pawns,
                'filter' : lambda val: pawns.index(val)
            }
        ]
        return prompt(question, style = style_from_dict(get_style()))['pawn']

    def ask_game_settings(self) :
        board_size_maps = {
            '8x8' : 8,
            '10x10' : 10,
            '16x16' : 16
        }

        bot_minimax = PlayerFactory().generate_player(Constant.MINIMAX)
        bot_minimax_local = PlayerFactory().generate_player(Constant.MINMAXWLOCAL)
        human = PlayerFactory().generate_player(Constant.NOBRAIN)

        game_mode_maps = {
            'bot vs human' : (bot_minimax, human),
            'bot with local search vs human' : (bot_minimax_local, human),
            'bot vs bot with local search' : (bot_minimax, bot_minimax_local) 
        }

        color_maps = {
            'red' : Color.RED,
            'green' : Color.GREEN
        }

        interface_maps = {
            "Graphical User Interface (GUI)" : "gui",
            "Command Line Interface (CLI)" : "cli"
        }

        question = [
            {
                'type' : 'list',
                'name' : 'interface',
                'message' : "Please choose an interface : ",
                'choices' : ["Command Line Interface (CLI)", "Graphical User Interface (GUI)"],
                'filter' : lambda val: interface_maps[val]
            },
            {
                'type': 'list',
                'name': 'size',
                'message': 'What board size do you want to play?',
                'choices': ['8x8', '10x10', '16x16'],
                'filter': lambda val: board_size_maps[val.lower()]
            },
            {
                'type': 'input',
                'name': 'time',
                'message': 'What is the time limit? (default:5) : ',
                'default' : '5',
                'validate': lambda val: val.isdigit()
            },
            {
                'type': 'list',
                'name': 'mode',
                'message': 'What mode do you want to play?',
                'choices': ['Bot vs Human', 'Bot with Local Search vs Human', 'Bot vs Bot with Local Search'],
                'filter': lambda val: game_mode_maps[val.lower()]
            }
        ]

        print("Please enter game settings :")
        answer = prompt(question, style = style_from_dict(get_style()))
        if repr(answer['mode'][0].brain) == Constant.NOBRAIN or repr(answer['mode'][1].brain) == Constant.NOBRAIN:
            color = prompt(
                {
                    'type': 'list',
                    'name': 'color',
                    'message': 'Please choose color for the player',
                    'choices': ['Red', 'Green'],
                    'filter': lambda val: color_maps[val.lower()]
                }, style = style_from_dict(get_style())
            )['color']
            answer['pcolor'] = color
        

        return answer

    def show_title(self, title = "HALMA CHECKER"):
        print(colored.cyan(pyfiglet.figlet_format(title, font = "slant")))

    def show_ending(self, ending = "Congratulations!!"):
        print(colored.red(pyfiglet.figlet_format(ending, font = "slant")))

    def show_winner(self, state):
        p1TotalTime = "-" if repr(state.player_1.brain) == Constant.NOBRAIN else '{:.3f}'.format(state.player_1.brain.total_computing_time)   
        p2TotalTime = "-" if repr(state.player_2.brain) == Constant.NOBRAIN else '{:.3f}'.format(state.player_2.brain.total_computing_time)
        if state.currentPlayer.color == Color.RED:
            print(colored.red(pyfiglet.figlet_format("RED WIN!", font = "slant")))
        elif state.currentPlayer.color == Color.GREEN:
            print(colored.green(pyfiglet.figlet_format("GREEN WIN!", font = "slant")))
        
        print("P1 Total Computing Time : " + p1TotalTime + " second(s)")
        print("P2 Total Computing Time : " + p2TotalTime + " second(s)")


    