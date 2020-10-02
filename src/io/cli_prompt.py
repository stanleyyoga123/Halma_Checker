import pyfiglet	
from clint.arguments import Args
from clint.textui import puts, colored
from PyInquirer import style_from_dict, Token, prompt

from src.factory import PlayerFactory
from src.constant import Constant
from .utils import get_style

class CLIPrompt():

    def __init__(self):
        pass

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