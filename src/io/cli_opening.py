import pyfiglet	
from clint.arguments import Args
from clint.textui import puts, colored
from PyInquirer import style_from_dict, Token, prompt

from .utils import get_style

class CLIOpening():
    def ask_game_mode(self):
        question = [
            {
                'type': 'list',
                'name': 'mode',
                'message': 'What mode do you want to play?',
                'choices': ['Bot vs Human', 'Bot with Local Search vs Human', 'Bot vs Bot with Local Search'],
                'filter': lambda val: self.map_answer(val)
            }
        ]
        answer = prompt(question, style = style_from_dict(get_style()))
        return answer['mode']

    def map_answer(self,keyword):
        return  {
            'bot vs human' : 0,
            'bot with local search vs human' : 1,
            'bot vs bot with local search' : 2 
        }.get(keyword)

    def show_title(self, title = "HALMA CHECKER"):
        print(colored.cyan(pyfiglet.figlet_format(title, font = "slant")))