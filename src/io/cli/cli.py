import pyfiglet	
from clint.arguments import Args
from clint.textui import puts, colored
from PyInquirer import style_from_dict, Token, prompt

from src.factory import PlayerFactory
from src.constant import Constant

from .utils import get_style

class CLI():
    def render(self, state):
        print(colored.green(str(state.board)))

    def input(self, state):
        pawns = [f"Pawns at {pawn.position}" for pawn in state.currentPlayer.pawns]
        i_choosed_pawn = self.ask_pawn(pawns)
        choosed_pawn = state.currentPlayer.pawns[i_choosed_pawn]

        possible_moves = state.board.possible_moves(choosed_pawn)
        possible_moves_str = [f"Pawn to {pawn.position}" for pawn in possible_moves]
        i_moved_pawn = self.ask_movement(possible_moves_str)

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

    def ask_game_mode(self):
        question = [
            {
                'type': 'list',
                'name': 'mode',
                'message': 'What mode do you want to play?',
                'choices': ['Bot vs Human', 'Bot with Local Search vs Human', 'Bot vs Bot with Local Search'],
                'filter': lambda val: self.map_answer(val.lower())
            }
        ]
        player1, player2 = prompt(question, style = style_from_dict(get_style()))['mode']
        return player1, player2

    def map_answer(self,keyword):
        return  {
            'bot vs human' : (PlayerFactory().generate_player(Constant.MINIMAX), PlayerFactory().generate_player(Constant.MINIMAX)),
            'bot with local search vs human' : (PlayerFactory().generate_player(Constant.MINMAXWLOCAL), PlayerFactory().generate_player(Constant.NOBRAIN)),
            'bot vs bot with local search' : (PlayerFactory().generate_player(Constant.MINIMAX), PlayerFactory().generate_player(Constant.MINMAXWLOCAL)) 
        }.get(keyword)

    def show_title(self, title = "HALMA CHECKER"):
        print(colored.cyan(pyfiglet.figlet_format(title, font = "slant")))

    def show_ending(self, ending = "Congratulations!!"):
        print(colored.red(pyfiglet.figlet_format(ending, font = "slant")))
    
    def select_interface(self):
        map = {
            "Graphical User Interface (GUI)" : "gui",
            "Command Line Interface (CLI)" : "cli"
        }
        question = [
            {
                'type' : 'list',
                'name' : 'interface',
                'message' : "Please choose an interface : ",
                'choices' : ["Command Line Interface (CLI)", "Graphical User Interface (GUI)"],
                'filter' : lambda val: map[val]
            }
        ]
        return prompt(question, style = style_from_dict(get_style()))['interface']
    


    