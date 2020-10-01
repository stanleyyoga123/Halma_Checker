import pyfiglet	
from clint.arguments import Args
from clint.textui import puts, colored
from PyInquirer import style_from_dict, Token, prompt

from src.model.board import Board
from src.model.player import Player 

from .utils import get_style

class CLIInput():
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


    def input(self, board, player):
        pawns = [f"Pawns at {pawn.position}" for pawn in player.pawns]
        i_choosed_pawn = self.ask_pawn(pawns)
        choosed_pawn = player.pawns[i_choosed_pawn-1]

        possible_moves = board.possible_moves(choosed_pawn)
        possible_moves_str = [f"Pawn to {pawn.position}" for pawn in possible_moves]
        i_moved_pawn = self.ask_movement(possible_moves_str)

        moved_pawn = possible_moves[i_moved_pawn-1] 
        print(f'You Choose Pawn from {choosed_pawn.position} Move to {moved_pawn.position}')
        print()

        return (choosed_pawn, moved_pawn)